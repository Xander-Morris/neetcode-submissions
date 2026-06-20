# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = -1
        # i use slow and fast pointers to easily get to the middle to break between the two sub-lists in the center
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # combine pairs
        curr = head

        while prev:
            res = max(res, curr.val + prev.val)
            curr = curr.next
            prev = prev.next

        return res