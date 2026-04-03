# Floyd Warshall
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float('inf')
        dist = [[inf]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        for u, v, w in times:
            dist[u-1][v-1] = w
        
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])
        shortest = max(dist[k-1])
        return shortest if shortest != inf else -1