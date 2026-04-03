class Point: 
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.distance = x**2 + y**2
    
class KClosestHeap:
    def __init__(self):
        self.points = []

    def add(self, point: Point):
        self.points.append(point)
        i = len(self.points) - 1
        parr = (i-1) // 2
        while parr > 0:
            if self.points[i].distance > self.points[parr].distance:
                self.points[i], self.points[parr] = self.points[parr], self.points[i]
                i = parr
            else:
                break
    def pop(self):
        print(len(self.points))
        for i in range(len(self.points)):
            print(self.points[i].x, " ", self.points[i].y)
        if not self.points:
            return None
        root = self.points[0]
        self.points[0] = self.points[-1]
        self.points.pop()

        curr = 0
        n = len(self.points)
        while True:
            left = curr * 2 + 1
            right = curr * 2 + 2
            smallest = curr

            if left < n and self.points[left].distance < self.points[smallest].distance:
                smallest = left
            if right < n and self.points[right].distance < self.points[smallest].distance:
                smallest = right

            if smallest != curr:
                self.points[curr], self.points[smallest] = self.points[smallest], self.points[curr]
                curr = smallest
            else:
                break
        return root

    def heapify(self, nums: List[List[int]]):
        for i in range(len(nums)):
            print(nums[i][0], nums[i][1])
            self.points.append(Point(nums[i][0], nums[i][1]))
            print("Distance: ", self.points[-1].distance)
        n = len(nums)
        run = n// 2 -1
        index = run
        while index >= 0:
            print('heapify curr: ', index)
            curr = index
            while True:
                left = curr * 2 + 1
                right = curr * 2 + 2
                smallest = curr
                if left < n and self.points[left].distance < self.points[smallest].distance:
                    smallest = left
                if right < n and self.points[right].distance < self.points[smallest].distance:
                    smallest = right
                # print(self.points[left].distance, " smallest ", self.points[smallest].distance)
                print("smallest and curr: ", smallest, " ", curr)
                if smallest != curr:
                    print("Smallest ", smallest)
                    self.points[curr], self.points[smallest] = self.points[smallest], self.points[curr]
                    curr = smallest
                else:
                    break
            for i in range(len(self.points)):
                print(self.points[i].x, " ", self.points[i].y)
            index -= 1
        return self.points        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kPoints = []
        kClosestHeap = KClosestHeap()
        kClosestHeap.heapify(points)
        for i in range(k):
            point = kClosestHeap.pop()
            if point:
                kPoints.append([point.x, point.y])
        return kPoints
        