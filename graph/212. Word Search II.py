'''
Xiaochi Ma
2018-12-07
'''

class Solution(object):
    
    def bfs(self, word, board, row, col, vis):
        if len(word) == 0:
            return True
        if row >= len(board) or row < 0:
            return False
        if col >= len(board[0]) or col < 0:
            return False
        if vis[row][col] == 1:
            return False
        vecs = [[-1, 0],[1, 0],[0, -1],[0, 1]]
        if word[0] == board[row][col]:
            vis[row][col] = 1
            for vec in vecs:
                b = []
                for arr in board:
                    b.append(arr[:])
                if self.bfs(word[1:], b, row+vec[0], col+vec[1], vis[:]):
                    return True
            vis[row][col] = 0
        else:
            return False
        
    
    def findWords(self, board, words):
        
        begins = {}
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        arr = begins.get(word, [])
                        arr.append([i, j])
                        begins[word] = arr
        res = []
        
        for word in set(words):
            if word in begins:
                for begin in begins[word]:
                    vis = [[0 for i in range(len(board[0]))] for j in range(len(board))]
                    if self.bfs(word, board, begin[0], begin[1], vis[:]):
                        res.append(word)
                        break
        return res
    
if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findWords([['o','a','a','n'],
                              ['e','t','a','e'],
                              ['i','h','k','r'],
                              ['i','f','l','v']], ["oath","pea","eat","rain"]))
    print(solution.findWords([['a','a']], ["aaa"]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    