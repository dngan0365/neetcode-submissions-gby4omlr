class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj[i] = set()
        for u, v in prerequisites:
            adj[v].add(u)

        preCourse = {}

        def dfs(node):
            if node in preCourse:
                return preCourse[node]
            preCourse[node] = set()
            for u in adj[node]:
                ancestor = dfs(u)
                preCourse[node] |= ancestor
                preCourse[node].add(u)
            return preCourse[node]

        for i in range(numCourses):
            dfs(i)
        print(preCourse)
        
        ans = []

        for u, v in queries:
            if u in preCourse[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans







