# BFS
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        
        # print(adj)

        maxHeap = [(-1, start_node)]
        largest = {}

        while maxHeap:
            s1, n1 = heapq.heappop(maxHeap)
            if (n1 not in largest) or (s1 > largest[n1]):
                largest[n1] = -s1
            for n2, s2 in adj[n1]:
                suc = abs(s1*s2)
                if (n2 not in largest) or (suc > largest[n2]):
                    heapq.heappush(maxHeap, (-suc, n2))
        # print(largest)

        return largest[end_node] if end_node in largest else 0