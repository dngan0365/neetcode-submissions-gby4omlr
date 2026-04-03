# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def dfs(output: List[int], root: Optional[TreeNode]):
            if not root:
                return None
            dfs(output, root.left)
            output.append(root.val)
            dfs(output, root.right)
        dfs(output, root)
        return output
        

        
        












# class Solution:
#     # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     #     nums = []
#     #     def inorder(node):
#     #         if not node:
#     #             return None
#     #         inorder(node.left)
#     #         nums.append(node.val)
#     #         inorder(node.right)
#     #     inorder(root)
#     #     return nums
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = []
#         curr = root
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             res.append(curr.val)
#             curr = curr.right
#         return res



