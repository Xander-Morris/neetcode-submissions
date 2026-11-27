# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []

        for head in lists:
            curr = head

            while curr:
                vals.append(curr.val)
                curr = curr.next
        
        vals = sorted(vals)

        if len(vals) == 0:
            return None

        head = ListNode(vals[0])
        prev = head

        for i in range(1, len(vals)):
            node = ListNode(vals[i])
            prev.next = node
            prev = node 
        
        return head 