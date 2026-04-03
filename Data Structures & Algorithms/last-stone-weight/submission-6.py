class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i] > self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def pop(self) -> int:
        if not self.heap:
            return -1
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        n = len(self.heap)
        while 2*i + 1 < n:
            left = 2*i + 1
            right = 2*i + 2
            largest = left
            if right < n and self.heap[right] > self.heap[left]:
                largest = right
            if self.heap[i] < self.heap[largest]:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break
        return ans

    def top(self) -> int:
        return self.heap[0] if self.heap else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums[:]
        n = len(self.heap)
        for i in range((n-2)//2, -1, -1):
            j = i
            while 2*j + 1 < n:
                left = 2*j + 1
                right = 2*j + 2
                largest = left
                if right < n and self.heap[right] > self.heap[left]:
                    largest = right
                if self.heap[j] < self.heap[largest]:
                    self.heap[j], self.heap[largest] = self.heap[largest], self.heap[j]
                    j = largest
                else:
                    break

    def lastStone(self) -> int:
        while len(self.heap) >= 2:
            x = self.pop()   # largest
            y = self.pop()   # second largest
            if x != y:
                self.push(abs(x - y))
        return self.heap[0] if self.heap else 0



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap()
        heap.heapify(stones)
        return heap.lastStone()

        