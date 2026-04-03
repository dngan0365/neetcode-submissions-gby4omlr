class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for _ in range(0, 32):
            if n & 1:
                total += 1
            n = n >> 1
        return total