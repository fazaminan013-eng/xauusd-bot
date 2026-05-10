import requests

class TelegramNotifier:

    def __init__(self, token, chat_id):

        self.token = token

        self.chat_id = chat_id

        self.url = f"https://api.telegram.org/bot{token}/sendMessage"

    def send_message(self, message):

        payload = {

            "chat_id": self.chat_id,

            "text": message,

            "parse_mode": "HTML"

        }

        try:

            response = requests.post(self.url, data=payload)

            if response.status_code != 200:

                print("Failed:", response.text)

        except Exception as e:

            print("Error sending message:", e)
