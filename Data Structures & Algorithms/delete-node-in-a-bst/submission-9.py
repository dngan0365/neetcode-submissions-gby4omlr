# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMinNode(self, root: Optional[TreeNode]):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_node = self.findMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root




















# class Solution:
#     def minValNode(self, root):
#         curr = root
#         while root and curr.left:
#             curr = curr.left
#         return curr

#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if not root:
#             return None

#         if root.val == key:
#             if root.left == None:
#                 root = root.right
#             elif root.right == None:
#                 root = root.left
#             else:
#                 min_node = self.minValNode(root.right)
#                 root.val = min_node.val
#                 root.right = self.deleteNode(root.right, min_node.val)
#         elif root.val > key:
#             root.left = self.deleteNode(root.left, key)
#         else:
#             root.right = self.deleteNode(root.right, key)
        
#         return root



