from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, async_to_sync
from time import sleep
import json
import asyncio



class OhlcvConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
#        await self.send(text_data="connected")
        await self.channel_layer.group_add("crypto_ohlcv", self.channel_name)

        print(f"Added {self.channel_name} channel to crypto_ohlcv")

        for i in range(10):
            await self.send(json.dumps({
                "type": "websocket.accept",
                # "send": {'text_data': str(i)}
                'text_data':str(i)
            }))
            # sleep(1)
            await asyncio.sleep(1)

            # await self.send(text_data=str(i))



    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("crypto_ohlcv", self.channel_name)
        print(f"Removed {self.channel_name} channel to crypto_ohlcv")





    
        
