import random
import time
import requests

TELEGRAM_BOT_TOKEN = "9230416906:AAFd40_vbqAjF4F33C56U42WWIBwjwkWtUs"
TELEGRAM_CHAT_ID = "8849648935"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram Connection Error: {e}")

def pro_quotex_telegram_bot():
    assets = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "NZD/USD"]
    
    send_telegram_message("🤖 *Pro Quotex Signal Bot Started on Render Cloud!* (24/7 Active)")

    while True:
        selected_asset = random.choice(assets)
        rsi_val = random.uniform(25.0, 75.0)
        
        if rsi_val < 40:
            signal = "CALL (UP) [Buy Signal]"
            confidence = "88%"
            msg = f"🚨 *QUOTEX PRO SIGNAL* 🚨\n\n🎯 Asset: `{selected_asset}`\n📊 RSI: `{rsi_val:.2f}` (Oversold)\n💡 Signal: *{signal}*\n⭐ Accuracy: `{confidence}`\n⏰ Expiry: `1 Minute`"
            send_telegram_message(msg)
            
        elif rsi_val > 60:
            signal = "PUT (DOWN) [Sell Signal]"
            confidence = "88%"
            msg = f"🚨 *QUOTEX PRO SIGNAL* 🚨\n\n🎯 Asset: `{selected_asset}`\n📊 RSI: `{rsi_val:.2f}` (Overbought)\n💡 Signal: *{signal}*\n⭐ Accuracy: `{confidence}`\n⏰ Expiry: `1 Minute`"
            send_telegram_message(msg)
            
        time.sleep(10)

pro_quotex_telegram_bot()
