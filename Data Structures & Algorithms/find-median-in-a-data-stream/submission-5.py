class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        if self.large and self.small and (self.large[0] < -1*self.small[0]):
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*temp)
        if len(self.small) - 1 > len(self.large):
            temp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*temp)
        if len(self.large) - 1 > len(self.small):
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*temp)            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1*self.small[0] + self.large[0]) / 2
        
        