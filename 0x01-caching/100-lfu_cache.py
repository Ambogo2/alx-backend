#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that inherits from BaseCaching.
        It uses an LFU algorithm to discard items when the cache limit is reached.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)  # Store frequency of each key
        self.order = OrderedDict()          # Store order of insertion for LRU fallback

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the limit, discard the least frequently used item (LFU).
            If there's a tie, discard the least recently used among those.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and frequency
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.order.move_to_end(key)  # Mark as recently used
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find least frequently used items
                    min_freq = min(self.frequency.values())
                    lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                    
                    # If multiple keys have the same frequency, use LRU to decide
                    if len(lfu_keys) > 1:
                        # Get the least recently used key among them
                        lfu_key = next(iter(self.order))  # The first one in order is LRU
                        for key in lfu_keys:
                            if key in self.order:
                                lfu_key = key if self.order[lfu_key] < self.order[key] else lfu_key
                        discarded_key = lfu_key
                    else:
                        discarded_key = lfu_keys[0]

                    # Discard the item
                    print(f"DISCARD: {discarded_key}")
                    self.cache_data.pop(discarded_key)
                    self.frequency.pop(discarded_key)
                    self.order.pop(discarded_key)

                # Add the new item
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.order[key] = item  # Insert the item in the order dict

    def get(self, key):
        """ Get an item by key.
            If key is None or doesn't exist, return None.
            Updates frequency and marks the key as recently used.
        """
        if key in self.cache_data:
            # Increment frequency and move to end to mark as recently used
            self.frequency[key] += 1
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
