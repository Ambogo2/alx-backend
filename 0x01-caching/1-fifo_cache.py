#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that inherits from BaseCaching.
        It uses a FIFO algorithm to discard items when the cache limit is reached.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []  # To keep track of the insertion order

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the limit, discard the first item added (FIFO).
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Discard the first item in the FIFO order
                    oldest_key = self.order.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")

            # Add or update the key in the cache
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)
            else:
                # Move the existing key to the end of the order
                self.order.remove(key)
                self.order.append(key)

    def get(self, key):
        """ Get an item by key.
            If key is None or doesn't exist, return None.
        """
        return self.cache_data.get(key)
