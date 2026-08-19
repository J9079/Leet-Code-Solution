# Question 1
# Link - https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# def sudoku(matrix):
#   rows=[set() for _ in range(9)]
#   cols=[set() for _ in range(9)]
#   boxes=[set() for _ in range(9)]


# Question 2
# Link - https://leetcode.com/problems/spiral-matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# def spiral(matrix):
#   top=0
#   left=0
#   right=len(matrix[0])-1
#   bottom=len(matrix)-1
#   result=[]
#   while left<=right and top<=bottom:
#     for i in range(left,right+1):
#       result.append(matrix[top][i])
#     top+=1  
#     for i in range(top,bottom+1):
#       result.append(matrix[i][right])
#     right-=1  
#     if left<=right:
#       for i in range(right,left-1,-1):
#         result.append(matrix[bottom][i])
#       bottom-=1
#     if  top<=bottom:
#       for i in range(bottom,top-1,-1):
#         result.append(matrix[i][left])
#       left+=1      
#   return result
# print(spiral([[1,2,3],[4,5,6],[7,8,9]]))

# Question 3
# Link - https://leetcode.com/problems/rotate-image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# def rotate(m):
#   for i in range(len(m)):
#     for j in range(i,len(m[i])):
#       temp=m[i][j]
#       m[i][j]=m[j][i]
#       m[j][i]=temp
#   for i in range(len(m)):
#     k=0 
#     j=len(m)-1
#     while k<j:
#       temp=m[i][k]
#       m[i][k]=m[i][j]
#       m[i][j]=temp
#       k+=1
#       j-=1    
#   return m
# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# def rotate_image(matrix):
#   for i in range(len(matrix[0])):
#     for j in range(i,len(matrix)):
#       temp=matrix[i]
#       matrix[i]=matrix[j]
#       matrix[j]=temp
#   return matrix
# print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))   


# def x(m):
#   r=0
#   l=0
#   for i in range(len(m)):
#     for j in range(len(m[i])):
#       if m[i]==m[j]:
#         l+=m[i][j]
#       if i+j==len(m)-1:
#         r+=m[i][j]
#   return l , r
# print(x([[1,2,3],[4,5,6],[7,8,9]]))      

# Question - 4
# Transpose Matrix
# https://leetcode.com/problems/transpose-matrix/description/
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]  
# def transpose(matrix):
#   ans=[[0]*len(matrix) for _ in range(len(matrix[0]))]
#   for i in range(len(ans)):
#     for j in range(len(ans[i])):
#       ans[i][j]=matrix[j][i]
#   return ans
# print(transpose([[1,2,3],[4,5,6],[7,8,9]])) 


  
# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         row=[set() for _ in range(9)]
#         col=[set() for _ in range(9)]
#         box=[set() for _ in range(9)]
#         for r in range(9):
#           for c in range(9):
#             value=board[r][c]
#             if value==".":
#               continue
#             boxi=  (r // 3) * 3 + (c // 3) 
# #           if value in row[r] or value in col[c] or value in box[boxi]:
# #             print(False) 
# #             exit()
# #           row[r].add(value)
# #           col[c].add(value)
# #           box[boxi].add(value)  
# #         print(True)           
# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         rows = [set() for _ in range(9)]
#         cols = [set() for _ in range(9)]
#         boxes = [set() for _ in range(9)]
#         for r in range(9):
#             for c in range(9):
#                 value = board[r][c]
#                 if value == ".":
#                     continue
#                 box_index = (r // 3) * 3 + (c // 3)
#                 if value in rows[r] or value in cols[c] or value in boxes[box_index]:
#                     return False
#                 rows[r].add(value)
#                 cols[c].add(value)
#                 boxes[box_index].add(value)
#         return True

# Question 1
# Link - https://leetcode.com/problems/set-matrix-zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# def zero(matrix):
#   row=[]
#   col=[]
#   for i in range(len(matrix)):
#       for j in range(len(matrix[0])):
#         if matrix[i][j]==0:
#           row.append(i)
#           col.append(j)
#   for i in row:
#     for j in range(len(matrix[0])):
#       matrix[i][j]=0
#   for j in col:
#     for i in range(len(matrix)):
#       matrix[i][j]=0      
#   return matrix
# print(zero([[1,1,1],[1,0,1],[1,1,1]]))  
      

# Question 2
# Link - https://leetcode.com/problems/game-of-life
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.
# Given the current state of the board, update the board to reflect its next state.
# Note that you do not need to return anything.
# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# def game(board):
#   count_one=0
#   count_zer=0
#   for i in range(len(board)):
#     for j in range(len(board[0])):
#       if board[i][j]==1:
#         count_one+=1
#       if board[i][j]==0:
#         count_zer+=1
#       if count_one==1 or count_zer==2:
#         board[i][j]=0
#       elif count_one==2 or count_zer==1:
#         board[i][j]=0
#       elif count_one==3 or count_zer==0:
#         board[i][j]=0

#   return board
# print(game([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

