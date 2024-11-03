#!/usr/bin/python3
"""MRU (Most Recently Used) caching module.
This module contains the MRUCache class which implements a caching system
with a Most Recently Used (MRU) eviction policy.
"""

from typing import Any
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a caching system with MRU eviction policy.

    Attributes:
        last_key (str): The key of the most recently used item.
    """

    def __init__(self) -> None:
        """
        Initialize the MRUCache instance and call the base class initializer.
        """
        super().__init__()
        self.last_key = None

    def put(self, key: str, item: Any) -> None:
        """Store an item in the cache using MRU policy.

        If the cache exceeds the maximum number of items, the most recently
        used item is discarded.

        Args:
            key (str): The key under which the item is stored.
            item (Any): The item to store in the cache.
        """
        if not key or not item:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.last_key = key
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_key = self.last_key
            self.cache_data.pop(discard_key)
            print(f'DISCARD: {discard_key}')

        self.last_key = key
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The item stored in the cache, or None if the key
            does not exist.
        """
        value = self.cache_data.get(key)
        if value:
            self.last_key = key

        return self.cache_data.get(key, None)
