class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node(0) 

    def get(self, index: int) -> int:
        curr = self.dummy
        
        for i in range(index + 1):
            if not curr:
                return -1
            curr = curr.next

        if not curr:
            return -1
        
        return curr.val 

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        prev_head = self.dummy.next
        self.dummy.next = new_node 

        if prev_head:
            new_node.next = prev_head 

    def addAtTail(self, val: int) -> None:
        tail = self.dummy

        while tail and tail.next:
            tail = tail.next
        
        tail.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy 

        for i in range(index):
            if not curr:
                return
            curr = curr.next

        if not curr:
            return

        prev_next = curr.next
        new_node = Node(val)
        curr.next = new_node

        if prev_next:
            new_node.next = prev_next 

    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy 

        for i in range(index):
            if not curr:
                return
            curr = curr.next
        
        if not curr:
            return 

        to_delete = curr.next
        if to_delete:
            curr.next = to_delete.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)