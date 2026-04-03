class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            if self.size[p_x] < self.size[p_y]:
                self.parent[p_x] = p_y
                self.size[p_y] += self.size[p_x]
            else:
                self.parent[p_y] = p_x
                self.size[p_x] += self.size[p_y]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        for u, v, w in edges:
            heapq.heappush(minHeap, (w, u, v))
        print(minHeap)
        unionFind = UnionFind(n)
        edges_used = 0
        count = 0
        while edges_used < n-1 and minHeap:
            curr = heapq.heappop(minHeap)
            isUnion = unionFind.union(curr[1], curr[2])
            if isUnion:
                edges_used += 1
                count += curr[0]
        return count if edges_used == n-1 else -1