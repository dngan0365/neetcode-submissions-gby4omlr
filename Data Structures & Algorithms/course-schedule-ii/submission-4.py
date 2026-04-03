class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        visited = set()
        visiting = set()
        sortCourses = []

        def dfs(pre: int):
            if pre in visited:
                return True
            if pre in visiting:
                return False
            visiting.add(pre)
            for u in adj[pre]:
                if not dfs(u):
                    return False
            visited.add(pre)
            visiting.remove(pre)
            sortCourses.append(pre)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        sortCourses.reverse()
        return sortCourses