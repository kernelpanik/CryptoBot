import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, async_to_sync


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
        await self.accept()
        await self.channel_layer.group_add("crypto_ohlcv", self.channel_name)
        print(f"Added {self.channel_name} channel to crypto_ohlcv")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("crypto_ohlcv", self.channel_name)
        print(f"Removed {self.channel_name} channel to crypto_ohlcv")

    async def receive(self, text_data=None, bytes_data=None):
        print(f"here")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            'crypto_ohlcv',
            {
                'type': 'get_price',
                'message': message
            }
        )

    async def get_price(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")


    
        
