# Install: pip install websocket-client asyncio
import asyncio
import json
import websocket
from typing import Dict

async def on_message(ws, message):
    data = json.loads(message)
    price = float(data["c"])  # Current price
    print(f"BTC/USD: {price}")
    # Feed to agents or DB here (e.g., Redis/TimescaleDB)

def on_error(ws, error):
    print(f"WebSocket Error: {error}")

def on_close(ws, *args):
    print("WebSocket Closed")

async def binance_websocket():
    url = "wss://stream.binance.com:9443/ws/btcusdt@ticker"
    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever()  # Runs in background

async def main():
    await asyncio.create_task(binance_websocket())

if __name__ == "__main__":
    asyncio.run(main())