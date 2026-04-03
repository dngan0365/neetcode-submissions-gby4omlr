class Solution:
    def isValidRate(self, piles: List[int], h: int, k: int):
        total_hours = 0
        for i in piles:
            total_hours+= math.ceil(i/k)
        return total_hours<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_banana_pile = max(piles)
        l, r = 1, max_banana_pile
        k = max_banana_pile
        while l<=r:
            m = (l+r)//2
            if self.isValidRate(piles, h, m):
                k=m
                r=m-1
            else:
                l=m+1
        return k
