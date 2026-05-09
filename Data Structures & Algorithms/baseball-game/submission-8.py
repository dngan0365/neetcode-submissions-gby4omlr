class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for i in operations:
            if i == '+':
                num1 = nums[-1]
                num2 = nums[-2]
                nums.append(num1+num2)
            elif i == 'C':
                nums.pop()
            elif i == 'D':
                nums.append(nums[-1]*2)
            else:
                nums.append(int(i))
        return sum(nums)