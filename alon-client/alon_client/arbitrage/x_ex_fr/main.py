import asyncio

from alon_client.arbitrage.x_ex_fr.arbitrage import FundingRateArbitrage
from alon_client.arbitrage.x_ex_fr.balancer import BalanceManager
from alon_client.arbitrage.x_ex_fr.config import configurations
from alon_client.arbitrage.x_ex_fr.exchange import initialize_exchange
from alon_client.arbitrage.x_ex_fr.funding_rate import FundingRateManager
from alon_client.arbitrage.x_ex_fr.utils import fetch_balance, transfer_funds

if __name__ == "__main__":
    # Initialize balance manager
    balance_manager = BalanceManager(
        exchanges_config=configurations["EXCHANGES"],
        fetch_balance=fetch_balance,
        transfer_funds=transfer_funds,
        config=configurations,
    )

    funding_rate_manager = FundingRateManager(
        check_interval=configurations["CHECK_INTERVAL"]
    )

    # Initialize arbitrage manager
    arbitrage = FundingRateArbitrage(
        exchanges_config=configurations["EXCHANGES"],
        initialize_exchange=initialize_exchange,
        start_balance_manager=balance_manager.run,
        funding_rate_collector=funding_rate_manager.collect_funding_rate,
        funding_rate_analyzer=funding_rate_manager.analyze_funding_rates,
        top_opportunities=configurations["TOP_OPPORTUNITIES"],
    )

    async def main():
        await asyncio.gather(
            balance_manager.run(),  # Run balance monitoring
            arbitrage.run(),  # Run funding rate arbitrage
        )

    asyncio.run(main())
