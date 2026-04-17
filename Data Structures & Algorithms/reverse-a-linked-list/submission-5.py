# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        """ 
            prev contains the head because prev = curr on the last iteration of the loop, 
            making it point to the last node, which is the head of the new list since we are reversing it
            1 -> 2 -> 3 becomes 3 -> 2 -> 1
            3 is the last node processed, which is what prev lands on, which is the new head 
        """
        return prev