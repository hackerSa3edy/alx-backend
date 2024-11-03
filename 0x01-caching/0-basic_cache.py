#!/usr/bin/python3
"""Basic dictionary caching module.
This module provides a simple caching system using a dictionary.
"""

from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system
    """

    def put(self, key, item) -> None:
        """ Store data in the dictionary.

        Args:
            key: The key under which the item should be stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key) -> Any:
        """ Get data from the dictionary.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item stored under the key, or None if the key does not exist.
        """
        if key:
            return self.cache_data.get(key, None)
