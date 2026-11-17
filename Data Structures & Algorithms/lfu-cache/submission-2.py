import heapq 

class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity 
        self._seq = 0
        self._min_heap = []
        self._mp = {}

    def get(self, key: int) -> int:
        if key not in self._mp:
            return -1
        
        self._seq += 1
        self._mp[key][1] += 1
        self._mp[key][2] = self._seq
        heapq.heappush(self._min_heap, (self._mp[key][1], self._mp[key][2], key)) 

        return self._mp[key][0]

    def put(self, key: int, value: int) -> None:
        if len(self._mp) == self._capacity and key not in self._mp:
            while self._min_heap:
                freq, seq, k = heapq.heappop(self._min_heap)

                if k not in self._mp or self._mp[k][1] != freq or self._mp[k][2] != seq:
                    continue

                del self._mp[k]
                break 

        self._seq += 1

        if key not in self._mp:
            self._mp[key] = [value, 1, self._seq]
        else:
            self._mp[key][0] = value 
            self._mp[key][1] += 1 
            self._mp[key][2] = self._seq 

        heapq.heappush(self._min_heap, (self._mp[key][1], self._mp[key][2], key))

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)