# telegram_bot.py

import telegram
import asyncio
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

async def send_telegram_alert(message, image_path):
    """
    Sends an image and a message to a specific Telegram chat.
    """
    if not TELEGRAM_TOKEN or TELEGRAM_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN":
        print("Error: Telegram token not configured in config.py")
        return
    if not TELEGRAM_CHAT_ID or TELEGRAM_CHAT_ID == "YOUR_TELEGRAM_CHAT_ID":
        print("Error: Telegram chat ID not configured in config.py")
        return

    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        # The library expects an asynchronous call
        await bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(image_path, 'rb'), caption=message)
        print(f"Alerta enviada a Telegram (Chat ID: {TELEGRAM_CHAT_ID})")
    except Exception as e:
        print(f"Error al enviar la alerta por Telegram: {e}")

if __name__ == '__main__':
    # This is for testing the Telegram bot functionality independently
    # Create a dummy image file to test
    import os
    if not os.path.exists("test_alert.jpg"):
        with open("test_alert.jpg", "w") as f:
            f.write("this is a test file")
            
    print("Probando el envío de una alerta a Telegram...")
    # To run this test, you need to have your credentials in config.py
    # and run `python telegram_bot.py` from your terminal.
    # Since this is an async function, we need to run it inside an event loop.
    asyncio.run(send_telegram_alert("Mensaje de prueba desde test", 'test_alert.jpg'))
    os.remove("test_alert.jpg")
