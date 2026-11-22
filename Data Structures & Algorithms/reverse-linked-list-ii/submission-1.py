# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 0
        curr = head
        start = None
        prev = None
        last_before_start = None 

        while curr:
            i += 1

            if i < left:
                last_before_start = curr
                curr = curr.next
                continue
            
            if i == left:
                start = curr 
            
            tmp = curr.next
            curr.next = prev 
            prev = curr

            if i == right:                
                if last_before_start:
                    last_before_start.next = curr 
                    print(last_before_start.val, last_before_start.next.val)
                start.next = tmp 
                break 
            
            curr = tmp 
        
        return curr if left == 1 else head 