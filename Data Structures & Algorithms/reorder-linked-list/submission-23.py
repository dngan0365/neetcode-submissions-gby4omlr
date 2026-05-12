# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next 
        # print(n)
        mid = n // 2
        node = head
        prev = None
        track = 0
        while track != mid:
            track += 1
            prev = node
            node = node.next
        # print(node.val)
        if prev:
            prev.next = None
        l1 = head
        l2 = node
        # Reverse l2
        temp = []
        while node:
            temp.append(node.val)
            node = node.next
        node = l2
        # print(temp)
        while node:
            node.val = temp.pop()
            node = node.next
        # print(l2.val)
        while l1 and l2:
            # insert an element from l2 to l1
            temp = l1.next
            old_l2 = l2
            l2 = l2.next
            l1.next = old_l2
            old_l2.next = temp
            old_l1 = l1.next
            l1 = temp
        if l2:
            # print(l2.val)
            # print(old_l1.val)
            old_l1.next = l2
        # return head

            
