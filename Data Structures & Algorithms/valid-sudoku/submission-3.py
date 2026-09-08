class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            dicti = defaultdict(int)
            dictj = defaultdict(int)
            for j in range(9):
                if board[i][j] != ".":
                    dicti[board[i][j]] += 1
                if(dicti[board[i][j]] > 1):
                    return False
                if board[j][i] != ".":
                    dictj[board[j][i]] += 1
                if(dictj[board[j][i]] > 1):
                    return False
        for i in range(3):
            for f in range (3):
                dicti.clear()
                for j in range(3):
                    for k in range(3):
                        if board[j + (i * 3)][k + (f * 3)] != ".":
                            dicti[board[j + (i * 3)][k + (f * 3)]] += 1
                        if(dicti[board[j + (i * 3)][k + (f * 3)]] > 1):
                            return False
        return True