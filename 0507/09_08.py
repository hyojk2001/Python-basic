import websockets
import asyncio

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws" #웹소켓 서버 주소

    async with websockets.connect(uri) as websocket:    #웹소켓 서버에 연결
        greeting = await websocket.recv()       #서버로부터 데이터 받음
        print(greeting)     #받은 데이터 출력

async def main():
    await bithumb_ws_client()

asyncio.run(main())