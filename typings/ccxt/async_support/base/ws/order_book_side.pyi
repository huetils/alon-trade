"""
This type stub file was generated by pyright.
"""

class OrderBookSide(list):
    side = ...
    def __init__(self, deltas=..., depth=...) -> None: ...
    def store_array(self, delta):  # -> None:
        ...
    def storeArray(self, delta):  # -> None:
        ...
    def store(self, price, size):  # -> None:
        ...
    def limit(self):  # -> None:
        ...
    def remove_index(self, order):  # -> None:
        ...
    def __len__(self):  # -> int:
        ...
    def __getitem__(self, item):  # -> list[list[Any] | Any]:
        ...
    def __eq__(self, other) -> bool: ...
    def __repr__(self):  # -> str:
        ...

class CountedOrderBookSide(OrderBookSide):
    def __init__(self, deltas=..., depth=...) -> None: ...
    def storeArray(self, delta):  # -> None:
        ...
    def store(self, price, size, count):  # -> None:
        ...

class IndexedOrderBookSide(OrderBookSide):
    def __init__(self, deltas=..., depth=...) -> None: ...
    def storeArray(self, delta):  # -> None:
        ...
    def remove_index(self, order):  # -> None:
        ...
    def store(self, price, size, order_id):  # -> None:
        ...

class Asks(OrderBookSide):
    side = ...

class Bids(OrderBookSide):
    side = ...

class CountedAsks(CountedOrderBookSide):
    side = ...

class CountedBids(CountedOrderBookSide):
    side = ...

class IndexedAsks(IndexedOrderBookSide):
    side = ...

class IndexedBids(IndexedOrderBookSide):
    side = ...
