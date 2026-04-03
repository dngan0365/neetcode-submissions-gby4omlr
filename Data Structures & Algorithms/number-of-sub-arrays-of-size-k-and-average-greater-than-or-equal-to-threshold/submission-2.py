class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        L, R = 0, 0
        currSum = 0
        ans = 0
        for i in range(0, k):
            currSum += arr[i]
            R += 1
        if currSum/k >= threshold:
            ans += 1
        for i in range(R, n):
            currSum -= arr[L]
            currSum += arr[i]
            L += 1
            if currSum/k >= threshold:
                ans += 1    
        return ans        
        