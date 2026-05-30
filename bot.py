"""
Hill Climb Racing Telegram Bot
================================
Termux mein chalane ke liye:
  pip install pyTelegramBotAPI flask requests
  python bot.py
"""

import telebot
import json
import os

# =============================================
# APNA TOKEN YAHAN DAALO
# BotFather se mila hua token
# =============================================
BOT_TOKEN = "APNA_BOT_TOKEN_YAHAN_DAALO"

# Aapki game ki URL (jahan HTML file host ki hai)
# Agar local server chal raha ho: "http://localhost:5000/game"
# Ya koi free hosting jaise: GitHub Pages, Netlify, etc.
GAME_URL = "https://APNI_GAME_URL.com/hill_climb_game.html"

# =============================================
bot = telebot.TeleBot(BOT_TOKEN)

# Players ka score store karne ke liye
scores = {}

@bot.message_handler(commands=['start'])
def start(msg):
    name = msg.from_user.first_name
    bot.send_message(
        msg.chat.id,
        f"🎮 *Hill Climb Racer mein Swagat hai {name}!* 🚗💨\n\n"
        "🕹️ *Kaise Khelen:*\n"
        "⛽ GAS button dabao - aage bado\n"
        "🔄 BRAKE button dabao - peeche jao\n"
        "₿ Coins collect karo - score badhao\n"
        "⛽ Fuel cans lo - aage bado\n\n"
        "🏆 Zyada door jao, zyada score pao!\n\n"
        "/play - Game shuru karo\n"
        "/score - Top scores dekho\n"
        "/help - Help",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['play'])
def play(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "🎮 GAME KHELO!",
            web_app=telebot.types.WebAppInfo(url=GAME_URL)
        )
    )
    bot.send_message(
        msg.chat.id,
        "🚗 *Hill Climb Racer*\n\nButton dabao aur game shuru karo! 🏔️",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['score'])
def show_scores(msg):
    if not scores:
        bot.send_message(msg.chat.id, "😅 Abhi tak kisi ne game nahi khela!\n/play karke pehle khelne wale bano!")
        return
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)
    text = "🏆 *TOP SCORES* 🏆\n\n"
    medals = ["🥇", "🥈", "🥉"]
    
    for i, (uid, data) in enumerate(sorted_scores[:10]):
        medal = medals[i] if i < 3 else f"{i+1}."
        text += f"{medal} *{data['name']}* - {data['score']} pts ({data['distance']}m)\n"
    
    bot.send_message(msg.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def help_cmd(msg):
    bot.send_message(
        msg.chat.id,
        "📖 *HELP*\n\n"
        "🎮 /play - Game shuru karo\n"
        "🏆 /score - Leaderboard dekho\n"
        "ℹ️ /start - Bot restart karo\n\n"
        "*Game Tips:*\n"
        "• Smooth gas dabane se car balance rehti hai\n"
        "• Steep hills par slowly jao\n"
        "• Fuel cans miss mat karna!\n"
        "• Coins dono score aur fun badhate hain 😄",
        parse_mode="Markdown"
    )

# WebApp se score receive karna
@bot.message_handler(content_types=['web_app_data'])
def web_app_data(msg):
    try:
        data = json.loads(msg.web_app_data.data)
        score = data.get('score', 0)
        distance = data.get('distance', 0)
        user_id = str(msg.from_user.id)
        name = msg.from_user.first_name
        
        # Score save karo
        if user_id not in scores or scores[user_id]['score'] < score:
            scores[user_id] = {'name': name, 'score': score, 'distance': distance}
            is_best = True
        else:
            is_best = False
        
        # Rank dhundho
        sorted_s = sorted(scores.values(), key=lambda x: x['score'], reverse=True)
        rank = next((i+1 for i, s in enumerate(sorted_s) if s['name'] == name), '?')
        
        msg_text = (
            f"🎮 *Game Over!*\n\n"
            f"📏 Distance: *{distance}m*\n"
            f"🏆 Score: *{score}*\n"
            f"📊 Aapki Rank: *#{rank}*\n"
        )
        if is_best:
            msg_text += "\n🎉 *Naya High Score! Shabaash!*"
        
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton("🔄 Dobara Khelo", web_app=telebot.types.WebAppInfo(url=GAME_URL)),
            telebot.types.InlineKeyboardButton("🏆 Scores", callback_data="show_scores")
        )
        
        bot.send_message(msg.chat.id, msg_text, reply_markup=keyboard, parse_mode="Markdown")
        
    except Exception as e:
        bot.send_message(msg.chat.id, "Score save karne mein problem aayi, lekin game khoob khela! 🎮")
        print(f"Error: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "show_scores")
def callback_scores(call):
    show_scores(call.message)

print("🚀 Hill Climb Racing Bot shuru ho gaya!")
print("Ctrl+C se band karo")
bot.infinity_polling()
