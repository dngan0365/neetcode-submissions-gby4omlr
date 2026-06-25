# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count length
        n_length = 0
        node = head
        while node:
            n_length += 1
            node = node.next
        # Remove head
        if n == n_length:
            return head.next
        # Find previous node
        track = 0
        n_remove = n_length - n - 1
        node = head
        while node and track != n_remove:
            node = node.next
            track += 1
        # Delete the node
        node.next = node.next.next
        return head
            