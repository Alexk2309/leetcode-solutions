#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        n = len(board)
        m = len(board[0])
        wordLen = len(word)

        def validLocation(row, col):
            if row < 0 or row >= n or col < 0 or \
            col >= m or tuple((row, col)) in visited:
                return False
            return True

        def search(row, col, index):
            if index == wordLen: return True
            if not validLocation(row, col) or board[row][col] != word[index]: return False
        
            visited.add(tuple((row, col)))
            res = search(row + 1, col, index + 1) or \
            search(row - 1, col, index + 1) or \
            search(row, col - 1, index + 1) or \
            search(row, col + 1, index + 1)
            visited.remove(tuple((row, col)))
            return res

        for i in range(n):
            for j in range(m):
                if search(i, j, 0): return True

        return False
            
        
# @lc code=end

