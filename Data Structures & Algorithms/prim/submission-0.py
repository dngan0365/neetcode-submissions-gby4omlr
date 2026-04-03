class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        minHeap = []
        for v, w in adj[0]:
            heapq.heappush(minHeap, [w, v])

        visit = set()
        visit.add(0)
        weights = 0
        
        while minHeap and len(visit) < n:
            curr = heapq.heappop(minHeap)
            w, u = curr[0], curr[1]
            if u in visit:
                continue
            visit.add(u)
            weights += w
            for v, w in adj[u]:
                heapq.heappush(minHeap, [w, v])
        
        return weights if len(visit) == n else -1

