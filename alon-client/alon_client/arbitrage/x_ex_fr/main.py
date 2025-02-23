import asyncio

from alon_client.arbitrage.x_ex_fr.arbitrage import funding_rate_arbitrage
from alon_client.arbitrage.x_ex_fr.config import configurations

if __name__ == "__main__":
    asyncio.run(*[funding_rate_arbitrage(configurations["EXCHANGES"])])
