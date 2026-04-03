class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        memo = [[0] * (n-1) for _ in range(2)]
        for i in range(0,n-1):
            if i%2 == 0:
                if arr[i] > arr[i+1]:
                    memo[1][i] = 1
                elif arr[i] < arr[i+1]:
                    memo[0][i] = 1
            else:
                if arr[i] < arr[i+1]:
                    memo[1][i] = 1
                elif arr[i] > arr[i+1]:
                    memo[0][i] = 1    
        print(memo)
        maxSum = 0
        currSum = 0
        for i in range(2):
            currSum = 0
            for j in range(0, n-1):
                if j!= 0 and memo[i][j] != memo[i][j-1]:
                    currSum = 0
                if memo[i][j] == 0:
                    currSum = 0
                currSum += memo[i][j]
                maxSum = max(currSum, maxSum)
            print(currSum)

        return maxSum + 1

