class MaxHeap:
    def __init__(self, k: int):
        self.nums = []
        self.k = k

    def add(self, val: int):
        self.nums.append(val)
        curr = len(self.nums) - 1

        # sift up
        while curr > 0:
            parent = (curr - 1) // 2
            if self.nums[curr] > self.nums[parent]:
                self.nums[curr], self.nums[parent] = self.nums[parent], self.nums[curr]
                curr = parent
            else:
                break

        if len(self.nums) > self.k:
            self._remove_min()

        print(self.nums)

    def _remove_min(self):
        # tìm phần tử nhỏ nhất trong maxheap
        min_idx = 0
        for i in range(1, len(self.nums)):
            if self.nums[i] < self.nums[min_idx]:
                min_idx = i

        # swap với cuối rồi pop
        self.nums[min_idx], self.nums[-1] = self.nums[-1], self.nums[min_idx]
        self.nums.pop()

    def pop(self) -> int:
        if len(self.nums) == 0:
            return
        elif len(self.nums) == 1:
            return self.nums.pop()
        ans = self.nums[0]
        self.nums[0] = self.nums.pop()
        n = len(self.nums) - 1
        curr = 0
        while 2*curr + 1 <= n:
            if 2*curr+2 <= curr \
                and self.nums[2*curr+2] > self.nums[curr]\
                and self.nums[2*curr+2] > self.nums[2*curr+1]:
                self.nums[2*curr+2], self.nums[curr] = self.nums[curr], self.nums[2*curr+2]
                curr = 2*curr+2
            elif self.nums[2*curr+1] > self.nums[curr]:
                self.nums[2*curr+1], self.nums[curr] = self.nums[curr], self.nums[2*curr+1]
                curr = 2*curr+1
            else:
                break
        return ans

    def heapify(self, nums: List[int]):
        self.nums = nums
        n = len(nums) - 1
        target = n//2 -1
        curr = target
        while curr >= 0:
            while 2*curr + 1 <= n:
                if 2*curr+2 <= curr \
                    and self.nums[2*curr+2] > self.nums[curr]\
                    and self.nums[2*curr+2] > self.nums[2*curr+1]:
                    self.nums[2*curr+2], self.nums[curr] = self.nums[curr], self.nums[2*curr+2]
                elif self.nums[2*curr+1] > self.nums[curr]:
                    self.nums[2*curr+1], self.nums[curr] = self.nums[curr], self.nums[2*curr+1]
                else:
                    break
            curr += 1
        

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = MaxHeap(k)
        for i in range(len(nums)):
            maxHeap.add(nums[i])
        for i in range(k):
            klargest = maxHeap.pop()
        return klargest
        