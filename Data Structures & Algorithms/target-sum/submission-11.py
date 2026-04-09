class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        old = {nums[0]: 1}
        if nums[0] == 0:
            old[0] = 2
        else:
            old[-nums[0]] = 1

        for i in range(1, n):
            new = {}
            for key in old:
                # dấu +
                new_key = key + nums[i]
                new[new_key] = new.get(new_key, 0) + old[key]

                # dấu -
                new_key = key - nums[i]
                new[new_key] = new.get(new_key, 0) + old[key]

            old = new

        return old.get(target, 0)