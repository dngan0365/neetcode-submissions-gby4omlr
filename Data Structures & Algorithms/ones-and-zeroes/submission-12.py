class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = []
        for i in range(len(strs)):
            count_ones = strs[i].count('1')
            count_zeros = strs[i].count('0')
            count.append((count_zeros, count_ones))
        print(count)
        dp = {}
        def dfs(i, m , n):
            if i == len(strs):
                return 0
            if m == 0 and n == 0:
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            
            res = dfs(i+1, m, n)
            if m >= count[i][0] and n >= count[i][1]:
                res = max(res, 1 + dfs(i+1, m - count[i][0], n - count[i][1]))
            dp[(i, m, n)] = res
            return res
        return dfs(0, m, n)