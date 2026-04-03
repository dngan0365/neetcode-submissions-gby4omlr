class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i in nums:
            nextperms = [] 
            for p in perms:
                for j in range(len(p)+1):
                    currp = p.copy()
                    currp.insert(j, i)
                    nextperms.append(currp)
                perms = nextperms 
        return perms