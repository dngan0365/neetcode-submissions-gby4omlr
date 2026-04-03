# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False]*n
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        def dfs(x:int):
            for i in adj[x]:
                if not visit[i]:
                    visit[i] = True
                    dfs(i)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res+=1
        return res