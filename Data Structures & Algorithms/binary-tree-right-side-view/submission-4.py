# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs_order = deque()
        right_side_view_list = []

        if root:
            bfs_order.append(root)
        

        while len(bfs_order)>0:
            one_level_list = []
            for i in range(len(bfs_order)):
                node = bfs_order.popleft()
                if node.left:
                    bfs_order.append(node.left)
                if node.right:
                    bfs_order.append(node.right)
                one_level_list.append(node.val)
            right_side_view_list.append(one_level_list[-1])
        return right_side_view_list    



















# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         queue = deque()
#         level = 0
#         right_side = []

#         if root:
#             queue.append(root)

#         while len(queue) > 0:
#             queue_len = len(queue)

#             for i in range(queue_len):
#                 curr = queue.popleft()
#                 if i == queue_len-1:
#                     right_side.append(curr.val)
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)

#             level += 1
         
#         return right_side


