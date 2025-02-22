"""
This type stub file was generated by pyright.
"""

import asyncio

class Future(asyncio.Future):
    is_race_future = ...
    def resolve(self, result=...):  # -> None:
        ...
    def reject(self, error=...):  # -> None:
        ...
    @classmethod
    def race(cls, futures):  # -> Future:
        ...
