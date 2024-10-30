#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache is a caching system that inherits from BaseCaching.
        It uses an LRU algorithm to discard items when the cache limit is reached.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to keep track of usage order

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the limit, discard the least recently used item (LRU).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and move it to the end of the order
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")

            # Insert or update the item and move it to the end as the most recently used
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.
            If key is None or doesn't exist, return None.
            Moves accessed item to the end as most recently used.
        """
        if key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
