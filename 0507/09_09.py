import websockets
import asyncio
import json

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws" 

    async with websockets.connect(uri, ping_interval=None) as websocket:    
        greeting = await websocket.recv()       
        print(greeting)     

        subscribe_fmt = {
            "type":"ticker",
            "symbols":["BTC_KRW"],
            "tickTypes":["1H"]
        }
        subscribe_data = json.dumps(subscribe_fmt)  #json을 이용해 파이썬 딕셔너리를 JSON 타입으로 변환
        await websocket.send(subscribe_data)        #구독 요청을 서버에 전송

        while True:
            data = await websocket.recv()   #빗썸 서버에서 데이터 받음
            data = json.loads(data)         #전달받은 JSON 타입의 데이터를 파이썬 딕셔너리 타입으로 변환
            print(data)

async def main():
    await bithumb_ws_client()

asyncio.run(main())