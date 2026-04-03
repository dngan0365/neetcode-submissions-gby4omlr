class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        alpha = set()
        rule = set()
        n = len(words)
        for i in range(n):
            for c in words[i]:
                alpha.add(c)
            if i < n-1: 
                j = i+1
                curr = 0
                while curr < len(words[i]) and curr < len(words[j]):
                    if len(words[i]) > len(words[j]) and words[i].startswith(words[j]):
                        return ""
                    if words[i][curr] != words[j][curr]:
                        rule.add((words[i][curr], words[j][curr]))
                        break
                    curr += 1
        # print(rule)
        # print(alpha)
        adj = defaultdict(list)
        for u, v in rule:
            adj[u].append(v)
        visited = set()
        visiting = set()
        topSort = []
        # print(adj)
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for u in adj[node]:
                if not dfs(u):
                    return False
            visiting.remove(node)
            visited.add(node)
            topSort.append(node)
            return True

        for i in alpha:
            # print(i)
            if not dfs(i):
                return ''
        topSort.reverse()
        return "".join(topSort)














