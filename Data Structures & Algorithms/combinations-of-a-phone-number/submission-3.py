class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = {}
        digit[2] = ['a', 'b', 'c']
        digit[3] = ['d', 'e', 'f']
        digit[4] = ['g', 'h', 'i']
        digit[5] = ['j', 'k', 'l']
        digit[6] = ['m', 'n', 'o']
        digit[7] = ['p', 'q', 'r', 's']
        digit[8] = ['t', 'u', 'v']
        digit[9] = ['w', 'x', 'y', 'z']

        ans = []
        
        def backtrack(i, curr):
            if len(curr) == len(digits):
                if len(curr) == 0:
                    return
                ans.append("".join(curr))
                return
            if i >= len(digits):
                return
            for j in digit[int(digits[i])]:
                curr.append(j)
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return ans 


        