class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        n = len(s1)
        m = len(s2)
        for i in range(0, m - n + 1):
            count2 = {}
            for c in s2[i:i+n]:
                count2[c] = 1 + count2.get(c, 0)
                # print(count2)
            if count2 == count1:
                return True
        return False