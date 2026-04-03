class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2!=0:
            return False
        open_brackets = ['(', '[', '{']
        valid = {
            '(': ')',
            '[': ']',
            '{': '}'
        } 
        stack=[]
        i=0
        while i<n:
            if s[i] in open_brackets:
                stack.append(s[i])
            elif not bool(stack):
                return False 
            elif valid[stack[-1]]==s[i]:
                stack.pop()
            else:
                return False
            i+=1
        if bool(stack):
            return False
        return True

