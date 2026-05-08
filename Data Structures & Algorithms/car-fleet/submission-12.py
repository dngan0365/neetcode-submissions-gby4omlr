class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        stack = []
        for i in range(0, len(pair)):
            temp = (target - pair[i][0]) / pair[i][1]
            if len(stack) == 0:
                stack.append(temp)
            elif not stack or temp > stack[-1]:
                stack.append(temp)
        print(stack)
        return len(stack)