#!/usr/bin/python3
"""LRU caching module.
This module implements an LRU (Least Recently Used) caching system.
"""
from typing import Any

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system.

    Inherits from BaseCaching and implements an LRU caching mechanism.
    """

    def __init__(self) -> None:
        """
        Initialize the LRUCache instance and call the base class initializer.
        """
        super().__init__()
        self.lru_keys = []

    def put(self, key, item) -> None:
        """ Store the data in the cache using LRU policy.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored.
        """
        if not key or not item:
            return

        if key in self.lru_keys:
            self.cache_data[key] = item

            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            self.cache_data.pop(self.lru_keys[0])
            print(f'DISCARD: {self.lru_keys[0]}')
            self.lru_keys.pop(0)

        self.lru_keys.append(key)
        self.cache_data[key] = item

    def get(self, key) -> Any:
        """ Get data from the cache using LRU policy.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        value = self.cache_data.get(key)
        if value:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)

        return self.cache_data.get(key, None)
