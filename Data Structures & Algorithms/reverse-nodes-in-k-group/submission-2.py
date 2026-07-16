# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    I came up with this solution off the top of the head with no cheating while in a NeetCode 1v1 competition
    in 16 minutes after trial and error for quite a lot of those 16 minutes. 
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = head
        curr = head

        # get entire length of linked list
        length = 0
        while curr:
            length += 1
            curr = curr.next

        curr = head
        last_node_in_last_part = None 
        # calculate number of full partitions from length of linked list
        parts = length // k
        
        for i in range(parts):
            prev = None 
            start_curr = curr # keep track of original "first" node in this part

            # reverse nodes 
            for j in range(k):
                tmp = curr.next
                curr.next = prev 
                prev = curr
                curr = tmp

            if last_node_in_last_part:
                # if there was a last node in last part, point its' next pointer to the first node in this new part
                last_node_in_last_part.next = prev  

            # last node in this part is what was originally the first node in this part since we reverse the nodes
            last_node_in_last_part = start_curr 

            if i == 0:
                # if this is first partition, then new head is prev
                new_head = prev

            if i == parts - 1:
                # if this is last part, then connect last node in it to curr node just in case there are any nodes left over in list
                start_curr.next = curr
        
        return new_head