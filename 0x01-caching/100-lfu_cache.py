#!/usr/bin/python3
""" LFU (Least Frequently Used) caching module.
This module contains the LFUCache class which implements a caching system
using the LFU (Least Frequently Used) policy.
"""
from typing import Any
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system.

    Inherits from BaseCaching and implements a caching system using
    the LFU policy.
    """

    def __init__(self) -> None:
        """ Initialize the LFUCache instance.

        Calls the parent class initializer and sets up the key frequency
        dictionary.
        """
        super().__init__()
        self.key_frequency = {}

    def put(self, key, item) -> None:
        """ Store an item in the cache using the LFU policy.

        If the cache exceeds the maximum number of items, it discards
        the least frequently used item.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.
        """
        if not key or not item:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.key_frequency[key] += 1
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_key = min(self.key_frequency, key=self.key_frequency.get)
            self.cache_data.pop(min_key)
            self.key_frequency.pop(min_key)
            print(f'DISCARD: {min_key}')

        self.key_frequency[key] = 1
        self.cache_data[key] = item

    def get(self, key) -> Any:
        """ Retrieve an item from the cache.

        If the key exists in the cache, its frequency count is incremented.

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the key, or None if the key
            does not exist.
        """
        value = self.cache_data.get(key)
        if value:
            self.key_frequency[key] += 1

        return self.cache_data.get(key, None)
