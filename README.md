## 🛠️ Setup Guide

To use this bot, you only need to do two things: Create a Telegram Bot and deploy the code.

### Step 1: Get Your Telegram Credentials
You will need two pieces of information from Telegram to make this work.

**1. Create a Bot (Get the Bot Token)**
* Open Telegram and search for **@BotFather**.
* Send the message `/newbot` and follow the instructions to give your bot a name and username.
* Once created, BotFather will give you a long API Token (it looks like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`). 
* Save this token. This is your `TELEGRAM_BOT_TOKEN`.

**2. Find Your Chat ID (Get the Chat ID)**
* Search for your newly created bot in Telegram and send it a message (like "hello").
* Next, search for **@userinfobot** in Telegram and start a chat with it.
* It will instantly reply with your `Id` (a string of numbers like `5457083826`). 
* Save this number. This is your `TELEGRAM_CHAT_ID`.

### Step 2: Deploy 24/7 (Railway.app)
The easiest way to run this without keeping your laptop open is using Railway. 

1. Create a free account on [Railway](https://railway.app/).
2. Click **New Project** -> **Deploy from GitHub repo** and select your repository.
3. Once the project is created, click on your Service and go to the **Variables** tab. Add the following:
   * `TELEGRAM_BOT_TOKEN` = (Paste the token from BotFather)
   * `TELEGRAM_CHAT_ID` = (Paste the ID from userinfobot)
4. **⚠️ CRITICAL STEP:** Go to the **Settings** tab in your Railway service, scroll down to the **Start Command** field, and type exactly: 
   `python monitor_usdc.py`
5. Click Save or let it auto-deploy. The service will build, and you will see "USDC ATA Monitor Started..." in your deployment logs!

---

### 🚨 Troubleshooting
**Error: "No start command detected / railpack process exited with an error"**
If you see a red failed build log on Railway, it means you forgot Step 3.4. Just go to **Settings**, find **Start Command**, type `python monitor_usdc.py`, and it will redeploy automatically!
