# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     res = []

    #     def inorder(node, res, k):
    #         if not node:
    #             return None
    #         node.left = inorder(node.left, res, k)
    #         res.append(node.val)
    #         # print(res)
    #         # if len(res) == k:
    #         #     return None
    #         node.right = inorder(node.right, res, k)

    #     inorder(root, res, k)

    #     return res[k-1]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            
            dfs(node.left)

            cnt -= 1
            
            if cnt == 0:
                res = node.val
                return
            
            dfs(node.right)

        dfs(root)

        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right







