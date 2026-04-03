# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class LinkList:
#     def __init__(self):
#         self.head = ListNode(-1)
#         self.tail = self.head
    
#     def get(self, index: int) -> int:
#         curr = self.head.next
#         i = 0
#         while curr:
#             if i == index: 
#                 return curr.val
#             i += 1
#             curr = curr.next
#         return -1

#     def insertHead(self, val: int) -> int:
#         new_node = ListNode(val)
#         new_node.next = self.head.next
#         self.head.next = new_node
#         if not new_node.next:
#             self.tail = new_node

#     def insertTail(self, val: int) -> int:
#         self.tail.next = ListNode(val)
#         self.tail = self.tail.next

#     def remove(self, index: int) -> int:
#         i = 0
#         curr = self.head
#         while i < index and curr:
#             i += 1
#             curr = curr.next

#         if curr and curr.next:
#             if curr.next == self.tail:
#                 self.tail = curr
#             curr.next = curr.next.next
#             return True
#         return False

#     def get(self) -> List[int]:
#         value = []
#         temp_node = self.head.next
#         while temp_node :
#             value.append(temp_node.val)
#             temp_node = temp_node.next
#         return value

#     def reverse(self):

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        temp = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = temp
            temp = temp.next
        return pre

            

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev, curr = None, head

#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
        
#         return prev

#     def reverseList_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head: 
#             return None
        
#         newHead = head
        
#         if head.next:
#             newHead = self.reverseList_v2(head.next)
#             head.next.next = head
#         head.next = None
#         return newHead

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre,cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre



