import os

from telegram import Bot

# =====================

# ENV dari Railway

# =====================

TOKEN = os.environ.get("TOKEN")

CHAT_ID = os.environ.get("CHAT_ID")

# =====================

# VALIDASI

# =====================

if not TOKEN or not CHAT_ID:

    print("❌ Missing TOKEN or CHAT_ID")

    exit()

# =====================

# INIT BOT

# =====================

bot = Bot(token=TOKEN)

# =====================

# SEND MESSAGE

# =====================

def start_bot():

    bot.send_message(

        chat_id=CHAT_ID,

        text="🚀 XAUUSD Bot IFVG sudah aktif di Railway!"

    )

# =====================

# MAIN

# =====================

def main():

    print("BOT STARTING...")

    start_bot()

    print("BOT RUNNING...")

if __name__ == "__main__":

    main()
