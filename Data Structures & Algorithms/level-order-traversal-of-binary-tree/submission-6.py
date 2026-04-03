# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        nums = []
        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            len_queue = len(queue)
            nums.append([])
            for i in range(len_queue):
                res = queue.popleft()
                nums[level].append(res.val)
                if res.left:
                    queue.append(res.left)
                if res.right:
                    queue.append(res.right)
            level += 1
        return nums
        
                