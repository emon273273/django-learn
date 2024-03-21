import sys

sys.stdout = open('output.txt', 'w')

sys.stdin = open('input.txt', 'r')

#adacency matrix

def printmatrix(matrix):
    r,c=len(matrix),len(matrix[0])

    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()


v,e=map(int,input().split())

matrix
