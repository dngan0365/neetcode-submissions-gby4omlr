class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        matches = 0
        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            # print(ord(s2[i]) - ord('a'))
            count2[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            matches += (1 if count1[i] == count2[i] else 0)
        # print("count1 ", count1)
        for i in range(n, m):
            # print(matches)
            if matches == 26:
                return True
            l = ord(s2[i-n]) - ord('a')
            r = ord(s2[i]) - ord('a')
            if l == r:
                continue
            if count2[l] == count1[l]:
                matches -= 1
            count2[l] -= 1
            if count2[l] == count1[l]:
                matches += 1
            
            if count2[r] == count1[r]:
                matches -= 1
            count2[r] += 1
            if count2[r] == count1[r]:
                matches += 1
        return matches == 26