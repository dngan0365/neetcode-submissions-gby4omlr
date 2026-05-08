class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pair = [(i, t) for i, t in enumerate(temperatures)]
        # print(pair)
        stack = [pair[0]]
        res = [0] * len(pair)
        for i in range(1, len(pair)):
            while True:
                if stack and pair[i][1] > stack[-1][1]:
                    # print(stack[-1][1])
                    res[stack[-1][0]] = pair[i][0] - stack[-1][0]
                    stack.pop()
                else:
                    break
            stack.append(pair[i])
        # print(res)
        return res