# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half.
        second = slow.next
        slow.next = None 
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 

        # Merge the two halves.
        first = head
        second = prev

        while second:
            """
                Start with:
                0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

                We now form:
                0 -> 6 -> 1
                We make the first node in the first half point to the last node in the last half
                Then, the last node in the last half has to point to what was originally the next node
                of the first node. 
                Since 0 pointed to 1, we now have 6 pointing to 1. 
            """
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1 
            first, second = temp_1, temp_2