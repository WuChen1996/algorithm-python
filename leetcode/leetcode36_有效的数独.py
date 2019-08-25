# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:16:19 2019

@author: qing
"""

class Solution:
    #三次迭代的笨方法
    def isValidSudoku_1(self, board) -> bool:
        #首先一排一排地扫描
        for i in range(9):
            temp = []
            for j in range(9):
                if board[i][j] not in temp:
                    temp.append(board[i][j])
                elif board[i][j] != '.':
                    return False
                
        #然后一列一列地扫描
        for i in range(9):
            temp = []
            for j in range(9):
                if board[j][i] not in temp:
                    temp.append(board[j][i])
                elif board[j][i] != '.':
                    return False
                
        #最后针对每个九宫格
        for z in range(3):
            for x in range(3):
                temp = []
                for i in range(3*z,3+3*z):
                    for j in range(3*x,3+3*x):
                        if board[i][j] not in temp:
                            temp.append(board[i][j])
                        elif board[i][j] != '.':
                            return False
        return True
    
    
    #一次迭代的官方解答
    def isValidSudoku_2(self, board) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    num = 5
                    i = 2
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True


        
s =Solution()
shudu = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]  
print(s.isValidSudoku_2(shudu))