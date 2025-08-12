# URL: https://leetcode.com/problems/lru-cache/description/

"""
LRUCache is an object. It contains capacity and an orderedDict that contains {'key': 'value'} pair O(1)
orderedDict to be able to do 'move_to_end'
"""

from collections import OrderedDict

class LRUCache:
    __slots__ = ('cap', 'od')
    # every LRUCache object will have these arguments, capacity + orderedDict
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()

    def put(self, key: int, value: int):
        '''doesn't return, only add key-value pair'''

        if key in self.od:
            # if this key exists, update value and its least recently used position
            self.od[key] = value
            self.od.move_to_end(key, last = False)
        else:
            # if it doesn't exist, check the capacity and update its LRU position
            if len(self.od) == self.cap:
                # if capacity is full, delete the latest LRU position
                self.od.popitem(last = True)
            self.od[key] = value
            self.od.move_to_end(key, last = False)

    def get(self, key: int) -> int:
        ''' Search in LRUCache object, use key to retrieve the value, change LRU Position'''

        if key not in self.od:
            # if such key doesn't exist
            return -1
        
        # if it does exist:
        # move the key to first position
        self.od.move_to_end(key, last = False)
        return self.od[key]
    
if __name__ == '__main__':

    sol = LRUCache(2)
    print(sol.put(1,1))
    print(sol.put(2,2))
    print(sol.get(1))
    print(sol.get(3))
    print(sol.put(3,3))
    print(sol.get(2))