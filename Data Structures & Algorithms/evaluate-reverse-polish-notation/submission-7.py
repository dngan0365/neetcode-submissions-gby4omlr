class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            print(stack)
            if i == '+' or i == '-'or i == '*' or i == '/':
                first = int(stack.pop())
                second = int(stack.pop())
                if i == '+':
                    temp = second + first
                elif i == '-':
                    temp = second - first
                elif i == '*':
                    temp = second * first
                elif i == '/':
                    temp = second / first
                stack.append(temp)
            else:
                stack.append(i)
        print(stack)
        return int(stack[-1])