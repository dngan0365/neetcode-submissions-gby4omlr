class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    def findRoot(self, num: int):
        curr = self.par[num]
        while curr != self.par[curr]:
            self.par[curr] = self.par[self.par[curr]]
            curr = self.par[curr]
        return curr

    def add(self, n1: int, n2: int):
        p1, p2 = self.findRoot(n1), self.findRoot(n2)
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

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)
        for x, y in edges:
            unionFind.add(x, y)
        count = 0
        root = set()
        for i in range(n):
            r = unionFind.findRoot(i)
            root.add(r)
        return len(root)


