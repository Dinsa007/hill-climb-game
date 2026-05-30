"""
Local Game Server
Termux mein chalao: python server.py
Game URL milegi: http://localhost:5000/game
"""
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/game')
def serve_game():
    return send_file('hill_climb_game.html')

@app.route('/')
def index():
    return "<h2>Hill Climb Bot Server Chal Raha Hai! 🚗</h2><a href='/game'>Game Khelo</a>"

if __name__ == '__main__':
    print("=" * 45)
    print("  Hill Climb Game Server Shuru Hua!")
    print("  Game URL: http://localhost:5000/game")
    print("  Telegram WebApp ke liye ngrok use karo")
    print("  ngrok http 5000")
    print("=" * 45)
    app.run(host='0.0.0.0', port=5000, debug=False)
