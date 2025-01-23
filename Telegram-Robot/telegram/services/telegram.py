import telepot
import requests
import config

from stackoverflow_service import StackOverFlowService


class TelegramBot():

    def __init__(self):
        self.telegram = telepot.Bot(
            config.TELEGRAM_CONNECTION
        )

    def send_msg(self, chat):
        type_text, priv, chat_id = telepot.glance(chat)
        
        service = StackOverFlowService(
            text=chat.get('text'), 
            type_text=type_text
        )
        results = service.get_messages_results()
        for msg in results:
            self.telegram.sendMessage(chat_id, msg)
        
    def received_msg(self):
        return self.telegram.message_loop(self.send_msg)

