#!/usr/bin/python3
"""FIFO caching module.

This module implements a FIFO (First-In-First-Out) caching system.
"""
from typing import Any

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system"""

    def __init__(self) -> None:
        """ Initialize the FIFO cache and call the base class initializer."""
        super().__init__()
        self.queue = []

    def put(self, key, item) -> None:
        """ Store the data in FIFO policy.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored.
        """
        if key is None or item is None:
            return

        if key in self.queue:
            self.cache_data[key] = item

            self.queue.remove(key)
            self.queue.append(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discard_element = self.queue.pop(0)
            self.cache_data.pop(discard_element)
            print(f'DISCARD: {discard_element}')

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key) -> Any:
        """ Get data from a FIFO cache system.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key
            does not exist.
        """
        return self.cache_data.get(key, None)
