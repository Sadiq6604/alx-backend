#!/usr/bin/python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """ LRU algorithm, handle elements """
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """ LRU algorithm, remove element """
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """ LRU algorithm, add element """
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

