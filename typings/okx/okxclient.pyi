"""
This type stub file was generated by pyright.
"""

from httpx import Client

class OkxClient(Client):
    def __init__(
        self,
        api_key=...,
        api_secret_key=...,
        passphrase=...,
        use_server_time=...,
        flag=...,
        base_api=...,
        debug=...,
        proxy=...,
    ) -> None: ...
