import asyncio

from alon_client.arbitrage.funding_rate.arbitrage import funding_rate_arbitrage
from alon_client.arbitrage.funding_rate.config import configurations

if __name__ == "__main__":
    asyncio.run(*[funding_rate_arbitrage(**ex) for ex in configurations["EXCHANGES"]])
