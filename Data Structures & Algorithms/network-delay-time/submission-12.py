class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        shortest = {node: float("inf") for node in range(1, n+1)}

        def dfs(node, time):
            if shortest[node] < time:
                return 
            shortest[node] = time
            for n, w in adj[node]:
                dfs(n, time + w)
        
        dfs(k, 0)
        res = max(shortest.values())
        return res if res < float('inf') else -1
