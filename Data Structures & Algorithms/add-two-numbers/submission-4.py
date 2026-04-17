# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # New digit to insert
            val = v1 + v2 + carry
            # The math below works since the constraints of the problem only
            # allow for the value of a node to be between 0 and 9 inclusive.
            # Hence, the maximum possible sum of two nodes is 18. 
            carry = val // 10 # The carry is the digit in the highest position.
            val = val % 10 # Take the digit in the ones place for the value.
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next