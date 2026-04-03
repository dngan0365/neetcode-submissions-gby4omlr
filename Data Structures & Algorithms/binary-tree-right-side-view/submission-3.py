# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        level = 0
        right_side = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            queue_len = len(queue)

            for i in range(queue_len):
                curr = queue.popleft()
                if i == queue_len-1:
                    right_side.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            level += 1
         
        return right_side


