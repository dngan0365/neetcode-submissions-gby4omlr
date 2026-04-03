class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, x: int) -> bool:
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        unionFind = UnionFind(n)
        latest = None
        for i in range(n):
            temp = unionFind.union(edges[i][0]-1, edges[i][1]-1)
            if temp == False:
                latest = edges[i]
        return latest




        