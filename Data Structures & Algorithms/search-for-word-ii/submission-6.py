class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def addWord(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        root = TrieNode()

        for w in words:
            root.addWord(w)
        # print(root)
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == rows or c == cols or
                board[r][c] not in node.children or (r, c) in visit
                ):
                return
            visit.add((r, c))
            curr_word = word + board[r][c]
            node = node.children[board[r][c]]
            if node.isEnd:
                res.add(curr_word)
            dfs(r-1, c, node, curr_word)
            dfs(r+1, c, node, curr_word)
            dfs(r, c-1, node, curr_word)
            dfs(r, c+1, node, curr_word)
            visit.remove((r, c))
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")
        return list(res)















