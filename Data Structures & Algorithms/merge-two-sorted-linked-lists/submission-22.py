# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
            
#         tail.next = list1 if list1 else list2
#         return dummy.next

#         return 

















class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        cur1, cur2 = list1, list2
        head = ListNode()
        cur = head
       
        while cur1 and cur2:
            if cur1.val<=cur2.val:
                cur.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val)
                cur2 = cur2.next

            cur = cur.next
        while cur1:
            cur.next = ListNode(cur1.val)
            cur1 = cur1.next
            cur = cur.next
        while cur2:
            cur.next = ListNode(cur2.val)
            cur2 = cur2.next
            cur = cur.next
        return head.next





            
                
        