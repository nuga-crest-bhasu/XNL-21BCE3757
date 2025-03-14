# Install: pip install aiokafka
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
import json

async def data_aggregator(producer: AIOKafkaProducer):
    # Simulate market data (replace with WebSocket feed)
    while True:
        data = {"symbol": "BTC/USD", "price": 60000 + random.randint(-100, 100)}
        await producer.send_and_wait("market_data", json.dumps(data).encode())
        await asyncio.sleep(1)

async def sentiment_analyzer(consumer: AIOKafkaConsumer, producer: AIOKafkaProducer):
    async for msg in consumer:
        price_data = json.loads(msg.value.decode())
        sentiment = await analyze_sentiment(f"BTC/USD at {price_data['price']}")
        await producer.send_and_wait("sentiment", json.dumps(sentiment).encode())

async def trade_decision(consumer: AIOKafkaConsumer):
    async for msg in consumer:
        sentiment = json.loads(msg.value.decode())
        action = "BUY" if sentiment["result"] == "POSITIVE" else "SELL"
        print(f"Trade Decision: {action}")

async def main():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
    market_consumer = AIOKafkaConsumer("market_data", bootstrap_servers='localhost:9092')
    sentiment_consumer = AIOKafkaConsumer("sentiment", bootstrap_servers='localhost:9092')

    await producer.start()
    await market_consumer.start()
    await sentiment_consumer.start()

    await asyncio.gather(
        data_aggregator(producer),
        sentiment_analyzer(market_consumer, producer),
        trade_decision(sentiment_consumer)
    )

if __name__ == "__main__":
    asyncio.run(main())