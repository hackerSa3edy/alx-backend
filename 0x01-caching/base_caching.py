#!/usr/bin/python3
""" BaseCaching module
This module provides a base class for caching systems.
It defines the basic structure and methods that any caching system
should implement.
"""


class BaseCaching:
    """ BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)

    Attributes:
        MAX_ITEMS (int): The maximum number of items the cache can hold.
        cache_data (dict): A dictionary to store the cache items.
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache data dictionary."""
        self.cache_data = {}

    def print_cache(self):
        """Print the current state of the cache.

        This method prints the keys and values of the items stored in the
        cache, sorted by the keys.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache.

        This method should be implemented by subclasses to add an item to
        the cache.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Raises:
            NotImplementedError: If the method is not implemented by
            the subclass.
        """
        raise NotImplementedError(
            'put must be implemented in your cache class'
            )

    def get(self, key):
        """Get an item by key.

        This method should be implemented by subclasses to retrieve an item
        from the cache.

        Args:
            key (str): The key of the item to be retrieved.

        Returns:
            any: The item stored in the cache, or None if the key
            does not exist.

        Raises:
            NotImplementedError: If the method is not implemented by
            the subclass.
        """
        raise NotImplementedError(
            'get must be implemented in your cache class'
            )
