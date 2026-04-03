class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        visited = set()
        visiting = set()

        def dfs(i, adj):
            if i in visited:
                return True
            if i in visiting:
                return False
            visiting.add(i)
            for v in adj[i]:
                if not dfs(v, adj):
                    return False
            visited.add(i)
            visiting.remove(i)
            return True
        
        for i in range(numCourses):
            if dfs(i, adj) == False:
                return False
        return True
