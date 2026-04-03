class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        preMap = {}

        def dfs(node: int):
            if node not in preMap:
                preMap[node] = set()
                for i in adj[node]:
                    preMap[node] |= dfs(i)
                preMap[node].add(node)
            return preMap[node]
        
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in preMap[v])
        return res







