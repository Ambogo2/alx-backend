#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from BaseCaching.
        It uses a LIFO algorithm to discard items when the cache limit is reached.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.last_key = None  # To track the last key added

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the limit, discard the last item added (LIFO).
        """
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item added
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            # Add or update the item in the cache
            self.cache_data[key] = item
            # Update the last key added
            self.last_key = key

    def get(self, key):
        """ Get an item by key.
            If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key)
