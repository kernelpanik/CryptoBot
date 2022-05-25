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
    async def connect(self):
        await self.channel_layer.group_add('crypto', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('crypto', self.channel_name)
        await self.disconnect()

    async def send_info(self, event):
        msg = event['text']
        await self.send(msg)        