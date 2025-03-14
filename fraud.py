async def detect_fraud(transaction: Dict) -> bool:
    # Dummy check: Flag if amount > $1M
    if transaction["amount"] > 1000000:
        return True
    return False

# Test
transaction = {"amount": 1500000, "desc": "Large BTC transfer"}
print(await detect_fraud(transaction))  # True