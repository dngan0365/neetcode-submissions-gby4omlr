# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.nums = []
        self.next_point = 0
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.nums.append(curr.val)
                curr = curr.right
 
    def next(self) -> int:
        self.next_point += 1
        return self.nums[self.next_point-1]

    def hasNext(self) -> bool:
        if self.next_point >= len(self.nums):
            return False
        return True
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        curr = node.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return val

    def hasNext(self) -> bool:
        if len(self.stack) == 0:
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()