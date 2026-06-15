class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s2)
        for i in range(0, n - len(s1) + 1):
            temp = s2[i : i + len(s1)]
            print(temp)
            temp = sorted(temp)
            if temp == s1:
                return True
        return False