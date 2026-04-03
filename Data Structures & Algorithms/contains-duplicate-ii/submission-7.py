class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        queue = deque()
        queue.append(nums[0])
        # print(queue)
        for i in range(1, n):
            if len(queue) > k:
                # print(queue)
                queue.popleft()
            if nums[i] in queue:
                return True
            else:
                queue.append(nums[i])
        return False
            