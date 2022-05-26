import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


# class OhlcvConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         self.send(text_data=json.dumps({
#             'message': message
#         }))

class OhlcvConsumer(AsyncWebsocketConsumer):

    groups = ["crypto_ohlcv"]

    async def connect(self):
        self.n  = 0
        await self.accept()
        await self.send(text_data='connected')

    async def receive(self, *, text_data):
        self.n += 1
        print(text_data)
        await self.send(text_data="echo: "+ str(self.n) + " " + text_data)
        
    async def disconnect(self, message):
        print('diconnect')