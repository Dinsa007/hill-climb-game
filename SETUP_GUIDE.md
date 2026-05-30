# 🎮 Hill Climb Racing Bot - Termux Setup Guide

## 📱 Step 1: Termux mein Install karo

```bash
# Packages update karo
pkg update && pkg upgrade -y

# Python install karo
pkg install python -y

# Pip tools install karo
pip install pyTelegramBotAPI flask requests
```

---

## 🤖 Step 2: Telegram Bot Banao

1. Telegram par **@BotFather** ko dhundho
2. `/newbot` type karo
3. Bot ka naam do (jaise: `My Hill Climb Bot`)
4. Username do (jaise: `myhillclimb_bot`)
5. **Token copy karo** (kuch aisa lagega):
   `1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ`

---

## 🌐 Step 3: Game Online Karo (2 tarike)

### Option A: GitHub Pages (FREE, Best)
1. GitHub account banao (github.com)
2. Naya repository banao: `hill-climb-game`
3. `hill_climb_game.html` upload karo
4. Settings → Pages → Branch: main → Save
5. URL milegi: `https://TUMHARA_USERNAME.github.io/hill-climb-game/hill_climb_game.html`

### Option B: ngrok (Local Server)
```bash
# ngrok install karo
pkg install wget -y
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar xvzf ngrok-v3-stable-linux-arm64.tgz

# Account banao: ngrok.com → token lo
./ngrok config add-authtoken TUMHARA_NGROK_TOKEN

# Server chalao (alag terminal mein)
python server.py &

# ngrok chalao
./ngrok http 5000
# URL milegi: https://xxxx.ngrok.io
# Game URL: https://xxxx.ngrok.io/game
```

---

## ⚙️ Step 4: Bot Configure karo

`bot.py` file mein ye 2 cheezein badlo:

```python
BOT_TOKEN = "TUMHARA_BOT_TOKEN_YAHAN"
GAME_URL = "https://TUMHARI_GAME_URL/hill_climb_game.html"
```

**Important:** Game URL HTTPS honi chahiye (Telegram WebApp ke liye zaroori hai)

---

## 🚀 Step 5: Bot Chalao

```bash
# Sab files ek folder mein rakho:
# - bot.py
# - hill_climb_game.html
# - server.py (agar local use kar rahe ho)

# Bot start karo
python bot.py
```

---

## 📂 Files Structure

```
mera-game/
├── bot.py                 # Telegram Bot
├── hill_climb_game.html   # Game
├── server.py              # Local Server (optional)
└── SETUP_GUIDE.md         # Ye guide
```

---

## 🎮 Bot Commands

| Command | Kaam |
|---------|------|
| `/start` | Bot shuru karo |
| `/play` | Game button aayega |
| `/score` | Top scores dekho |
| `/help` | Help |

---

## ❓ Problems & Solutions

**❌ "Module not found" error:**
```bash
pip install pyTelegramBotAPI flask
```

**❌ "Unauthorized" error:**
Bot token galat hai, dobara BotFather se lo

**❌ WebApp kaam nahi kar raha:**
Game URL HTTP hai, HTTPS chahiye. GitHub Pages use karo.

**❌ Score save nahi ho raha:**
Normal hai - ye simple version hai, score sirf tab tak rehta hai jab tak bot chalta hai. Permanent storage ke liye SQLite add karo.

---

## 💡 Tips

- Raat ko Termux band mat karo jab bot chal raha ho
- Background mein chalane ke liye: `nohup python bot.py &`
- Log dekhne ke liye: `tail -f nohup.out`

---

**Maza karo! 🚗💨🏔️**
