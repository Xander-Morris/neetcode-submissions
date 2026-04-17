# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(l):
            curr = l
            num_str = ""

            while curr:
                num_str += str(curr.val)
                curr = curr.next
            
            return int(num_str[::-1])

        num_1 = getNum(l1)
        num_2 = getNum(l2)
        sum_res = str(num_1 + num_2)
        head = ListNode(int(sum_res[-1]))
        last = head
        i = len(sum_res) - 2

        while i >= 0:
            node = ListNode(int(sum_res[i]))
            last.next = node
            last = node
            i -= 1

        return head
        