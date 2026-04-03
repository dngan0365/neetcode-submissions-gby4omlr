class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def countOne(num: int) -> int:
            res = 0
            while num:
                num &= num-1
                res += 1
            return res
        for i in range(n+1):
            ans.append(countOne(i))
        return ans
        