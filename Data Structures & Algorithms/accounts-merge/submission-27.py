# DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailIdx = {} # eamil => emailId
        emails = [] # Luu tat ca email xuat hien
        emailToAcc = {} # emailId => accountId 
        m = 0
        for i in range(len(accounts)):
            num_emails = len(accounts[i])
            account = accounts[i][0]
            for j in range(1, num_emails):
                if accounts[i][j] in emailIdx:
                    continue
                emails.append(accounts[i][j])
                emailIdx[accounts[i][j]] = m
                emailToAcc[m] = i
                m += 1
        adj = [[] for i in range(m)] 
        for a in accounts:
            for i in range(2, len(a)):
                idx1 = emailIdx[a[i]]
                idx2 = emailIdx[a[i-1]]
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)
        emailGroup = defaultdict(list) # index of acc -> list of emails
        visited = [False]*m
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)
        
        for i in range(m):
            if not visited[i]:
                dfs(i, emailToAcc[i])
        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))
        return res









