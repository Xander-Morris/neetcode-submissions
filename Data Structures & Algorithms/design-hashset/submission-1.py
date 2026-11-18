from collections import defaultdict

class MyHashSet:

    def __init__(self):
        self._bucket_size = 97
        self._mp = defaultdict(set)

    def _get_index(self, key: int) -> None:
        return key % self._bucket_size

    def add(self, key: int) -> None:
        idx = self._get_index(key)
        self._mp[idx].add(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        idx = self._get_index(key)
        self._mp[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._get_index(key)

        return key in self._mp[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)