class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
        visited = set()
        visiting = set()
        topSort = []

        def dfs(src: int) -> bool:
            if src in visited:
                return True
            if src in visiting:
                return False
            visiting.add(src)
            for n in adj[src]:
                if not dfs(n):
                    return False
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort
        