class MedianFinder:
    def __init__(self):
        self.nums = []
    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
    def findMedian(self) -> int:
        n = len(self.nums)
        if n%2 == 0:
            right = n//2
            left = right -1
            mid = (self.nums[right] + self.nums[left])/2
        else:
            mid = self.nums[n//2]
        return mid

    