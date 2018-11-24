'''
Xiaochi Ma
2018-11-16
'''

class Solution:
    
    def bfs(self, board, word, pos, cur, visited):
        
        if pos == len(word):
            return True
        
        nrow = len(board)
        ncol = len(board[0])
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nextCor = [cur[0]+dx[i], cur[1]+dy[i]]
            if nextCor[0] >= 0 and nextCor[0] < nrow and nextCor[1] >= 0 and nextCor[1] < ncol:
                if nextCor not in visited and board[nextCor[0]][nextCor[1]] == word[pos]:
                    visited.append(nextCor)
                    tag = self.bfs(board, word, pos+1, nextCor, visited)
                    if tag:
                        return True
                    visited.pop()
    
    def exist(self, board, word):
        
        if len(word) == 0:
            return False
        
        nrow = len(board)
        ncol = len(board[0])
        
        key = word[0]
        
        targets = []
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == key:
                    targets.append([i, j])
                    
        if len(targets) == 0:
            return False
        
        for cur in targets:
            tag = self.bfs(board, word, 1, cur, [cur])
            if tag:
                return True
        
        return False
    
if __name__ == '__main__':
    
    solution = Solution()
#    print(solution.exist([
#                          ['A','B','C','E'],
#                          ['S','F','C','S'],
#                          ['A','D','E','E']
#                        ],"SFDC")) 
    print(solution.exist([["a","a"]], "aaa")) 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    