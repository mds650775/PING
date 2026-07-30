import asyncio
import json
import os
import requests
import websockets
from solders.pubkey import Pubkey
from solders.system_program import ID as SYSTEM_PROGRAM_ID
from solders.token.associated import get_associated_token_address

# ============== CONFIG ==============
WALLET_ADDRESS = "5ez2dy3H3RQjadBkrDJwFKhiB6avvDC92cZQ9YMobVM2"
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
# ===================================

# Derive USDC Associated Token Account (ATA)
wallet_pubkey = Pubkey.from_string(WALLET_ADDRESS)
usdc_mint_pubkey = Pubkey.from_string(USDC_MINT)
USDC_ATA = str(get_associated_token_address(wallet_pubkey, usdc_mint_pubkey))

print(f"Monitoring USDC ATA: {USDC_ATA}")

seen_signatures = set()

def send_telegram(sig: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram config missing")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    message = f"🚨 <b>USDC Movement Detected!</b>\n\nTx: https://solscan.io/tx/{sig}"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
        print("✅ Telegram notification sent")
    except Exception as e:
        print("Failed to send Telegram:", e)

async def monitor():
    print("🚀 USDC ATA Monitor Started...")
    reconnect_delay = 5

    while True:
        try:
            async with websockets.connect("wss://api.mainnet-beta.solana.com") as ws:
                # Subscribe to account changes on the USDC ATA
                subscribe_msg = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "accountSubscribe",
                    "params": [
                        USDC_ATA,
                        {"commitment": "confirmed", "encoding": "jsonParsed"}
                    ]
                }
                await ws.send(json.dumps(subscribe_msg))
                print(f"✅ Subscribed to USDC ATA: {USDC_ATA}")

                async for message in ws:
                    try:
                        data = json.loads(message)
                        if 'params' not in data:
                            continue

                        result = data['params'].get('result', {})
                        signature = result.get('value', {}).get('signature')  # May not always be present

                        if signature and signature in seen_signatures:
                            continue
                        if signature:
                            seen_signatures.add(signature)

                        print(f"✅ USDC Balance Change Detected! Tx: {signature or 'Unknown'}")
                        send_telegram(signature or "recent-tx")
                    except:
                        continue

        except Exception as e:
            print(f"Connection lost: {e}. Reconnecting in {reconnect_delay}s...")
            await asyncio.sleep(reconnect_delay)
            reconnect_delay = min(reconnect_delay * 2, 60)

if __name__ == "__main__":
    asyncio.run(monitor())
