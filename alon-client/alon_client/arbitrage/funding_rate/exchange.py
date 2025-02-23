import ccxt.pro
from ccxt.base.exchange import Exchange


async def initialize_exchange(
    exchange_id: str, api_key: str, api_secret: str, api_password: str
) -> Exchange:
    """
    Initialize and return a CCXT Pro exchange instance.
    """
    try:
        exchange = getattr(ccxt.pro, exchange_id)(
            {
                "apiKey": api_key,
                "secret": api_secret,
                "password": api_password,
                "enableRateLimit": True,
            }
        )
        return exchange
    except AttributeError as e:
        raise ValueError(f"Exchange {exchange_id} is not supported.") from e
