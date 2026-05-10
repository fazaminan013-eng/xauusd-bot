import os
from telegram_notifier import TelegramNotifier

def main():
    TOKEN = os.environ.get("TOKEN")
    CHAT_ID = os.environ.get(6468207840)

    if not TOKEN or not CHAT_ID:
        print("Missing TOKEN or CHAT_ID")
        return

    bot = TelegramNotifier(TOKEN, CHAT_ID)
    bot.send_message("🚀 Bot XAU IFVG sudah aktif di Railway!")

    print("BOT RUNNING")

if __name__ == "__main__":
    main()
