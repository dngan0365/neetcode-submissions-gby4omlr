class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]
        n = len(temperatures)
        for i in range(n-2, -1, -1):
            for j in range(i+1, n+1):
                # print(i, " ", j)
                if j == n:
                    res.append(0)
                    break
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
        # print(res)
        return res[::-1]