import websockets
import asyncio

async def handle_commands(websocket, path):
    async for message in websocket:
        # 处理命令
        if message == "screenshot":
            # 执行截图操作
            pass
        elif message.startswith("click:"):
            # 解析点击坐标并执行点击操作
            pass
        elif message.startswith("drag:"):
            # 解析拖拽坐标并执行拖拽操作
            pass

start_server = websockets.serve(handle_commands, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()