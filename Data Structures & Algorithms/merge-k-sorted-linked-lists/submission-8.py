# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None
#         for i in range(1, len(lists)):
#             lists[i] = self.merge(lists[i-1], lists[i])
#         return lists[-1]
        
#     def merge(self, l_list: Optional[ListNode], r_list: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while l_list and r_list:
#             if l_list.val < r_list.val:
#                 tail.next = l_list
#                 l_list = l_list.next
#             else:
#                 tail.next = r_list
#                 r_list = r_list.next
#             tail = tail.next
#         if l_list:
#             tail.next = l_list
#         if r_list:
#             tail.next = r_list
#         return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i-1], lists[i])
            
        return lists[-1]

    def merge(self, l: Optional[ListNode], r: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        if l:
            tail.next = l
        if r:
            tail.next = r
        return dummy.next
