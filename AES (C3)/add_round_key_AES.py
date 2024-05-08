#from pwn import xor #su dung c2
from operator import xor #su dung c1
import numpy
import sys  
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
matrix = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
        ]    
def matrix2bytes(matrix):
    for i in matrix:
        for j in i:
            print(chr(j), end="")

def add_round_key(s, k):
  
    for i in range(4):
        for j in range(4):
            matrix[i][j]= xor(s[i][j], k[i][j]) ##cach 1 
    return matrix2bytes(matrix)
    
# def add_round_key(s, k):
#     return xor (s,k) ##cach 2
# print(add_round_key(state, round_key))

