class TelegramNotifier:

    def __init__(self, token):

        self.token = token

    def send(self, text):

        print("send:", text)
