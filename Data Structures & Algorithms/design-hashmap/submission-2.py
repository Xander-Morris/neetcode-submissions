from dataclasses import dataclass

@dataclass
class ListNode:
    key: int 
    value: int 
    next: ListNode

class MyHashMap:
    buckets = pow(10, 4)

    @classmethod 
    def get_index(cls, key: int):
        return key % MyHashMap.buckets 

    def __init__(self):
        self._nodes = [ListNode(-1, -1, None) for _ in range(MyHashMap.buckets)]

    def put(self, key: int, value: int) -> None:
        idx = MyHashMap.get_index(key)
        curr = self._nodes[idx]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next.value = value 
                return  
            curr = curr.next
        
        curr.next = ListNode(key, value, None)

    def get(self, key: int) -> int:
        idx = MyHashMap.get_index(key)
        curr = self._nodes[idx]

        if not curr.next:
            return -1

        while curr and curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        idx = MyHashMap.get_index(key)
        curr = self._nodes[idx]

        while curr and curr.next:
            if curr.next.key == key:
                tmp = curr.next
                curr.next = curr.next.next
                del tmp 
                return 
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)