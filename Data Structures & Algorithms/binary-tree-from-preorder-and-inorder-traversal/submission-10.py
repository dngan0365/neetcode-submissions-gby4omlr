# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        if (len(preorder)==1):
            return TreeNode(preorder[0])
        if (len(preorder)>0):
            root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        len_sub_left = root_index
        len_sub_right = len(inorder) - root_index 
        preorder.pop(0)
        root.left = self.buildTree(preorder[:len_sub_left], inorder[:root_index])
        root.right = self.buildTree(preorder[len_sub_left:], inorder[root_index+1:])
        return root
        
      



















# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None
        
#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

#         return root

#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         indices = {val: idx for idx, val in enumerate(inorder)}

#         self.pre_idx = 0

#         def dfs(l, r):
#             if l > r:
#                 return None
            
#             root_val = preorder[self.pre_idx]
#             self.pre_idx += 1
#             root = TreeNode(root_val)
#             mid = indices[root_val]
#             root.left = dfs(l, mid-1)
#             root.right = dfs(mid+1, r)
#             return root
        
#         return dfs(0, len(inorder)-1)

        