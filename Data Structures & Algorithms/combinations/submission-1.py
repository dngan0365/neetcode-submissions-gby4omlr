class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr = []
        def backtrack(i, curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            if i > n:
                return
            curr.append(i)
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
        backtrack(1, curr)
        return ans