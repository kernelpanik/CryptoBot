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
        await self.accept()
        await self.send(text_data='connected')

    async def receive(self, *, text_data):
#        await self.send(text_data='Hello world')
        await self.send(text_data)
        
    async def disconnect(self, message):
        print('diconnect')