"""
This type stub file was generated by pyright.
"""

class OrderBook(dict):
    def __init__(self, snapshot=..., depth=...) -> None: ...
    def limit(self):  # -> Self:
        ...
    def reset(self, snapshot=...):  # -> None:
        ...
    def update(self, snapshot):  # -> Self | None:
        ...

class CountedOrderBook(OrderBook):
    def __init__(self, snapshot=..., depth=...) -> None: ...

class IndexedOrderBook(OrderBook):
    def __init__(self, snapshot=..., depth=...) -> None: ...
