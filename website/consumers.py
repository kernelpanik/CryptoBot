from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, async_to_sync


class OhlcvConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="connected")
        await self.channel_layer.group_add("crypto_ohlcv", self.channel_name)
#        await self.channel_layer.group_add("crypto_ohlcv", "test")

        print(f"Added {self.channel_name} channel to crypto_ohlcv")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("crypto_ohlcv", self.channel_name)
        print(f"Removed {self.channel_name} channel to crypto_ohlcv")





    
        
