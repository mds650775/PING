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

### Step 2: Configure the Script
If you are running this locally on your computer, open `monitor_usdc.py` and replace `WALLET_ADDRESS` with the Solana wallet you want to track.

### Step 3: Deploy 24/7 (Railway.app)
The easiest way to run this without keeping your laptop open is using Railway. 

1. Create a free account on [Railway.app](https://railway.app/).
2. Click **New Project** -> **Deploy from GitHub repo** and select this repository.
3. Once it deploys, go to your Project's **Variables** tab.
4. Add the following variables:
   * `TELEGRAM_BOT_TOKEN` = (Paste the token from BotFather)
   * `TELEGRAM_CHAT_ID` = (Paste the ID from userinfobot)
5. Go to the **Settings** tab, scroll down to **Start Command**, and type: `python monitor_usdc.py`

The service will restart automatically, and you are good to go!
