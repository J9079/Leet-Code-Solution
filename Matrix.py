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
# def rotate_image(matrix):
#   for i in range(len(matrix[0])):
#     for j in range(i,len(matrix)):
#       temp=matrix[i]
#       matrix[i]=matrix[j]
#       matrix[j]=temp
#   return matrix
# print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))    