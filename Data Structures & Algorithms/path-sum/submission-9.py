# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         path = []
#         path_value = []

#         def pathSum(root: Optional[TreeNode], targetSum: int,  
#                     path: List[TreeNode], path_value: List[int]) -> bool:
            
#             if not root and sum(path_value) == targetSum:
#                 print(sum(path_value))
#                 print("path")
#                 print(path_value)
#                 return True
#             elif not root:
#                 return False
            
#             path.append(root)
#             path_value.append(root.val)

#             # if not root.left and not root.right:
#             #     return True
#             if pathSum(root.left, targetSum, path, path_value):
#                 return True
#             if pathSum(root.right, targetSum, path, path_value):
#                 return True

#             path.pop()
#             path_value.pop()
#             return False

#         return pathSum(root, targetSum, path, path_value)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        path_value = []

        def pathSum(root: Optional[TreeNode]) -> bool:
            if not root:
                return False

            path.append(root)
            path_value.append(root.val)

            # Check at leaf node
            if not root.left and not root.right and sum(path_value) == targetSum:
                print("Found path:", [n.val for n in path])
                path.pop()
                path_value.pop()
                return True

            found = pathSum(root.left) or pathSum(root.right)

            path.pop()
            path_value.pop()
            return found

        return pathSum(root)

