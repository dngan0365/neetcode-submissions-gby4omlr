# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(node, res, k):
            if not node:
                return None
            node.left = inorder(node.left, res, k)
            res.append(node.val)
            # print(res)
            # if len(res) == k:
            #     return None
            node.right = inorder(node.right, res, k)

        inorder(root, res, k)

        return res[k-1]