from sys import stdin

def wavePrint(mat, nRows, mCols):
    
    i=-1
    j=0
    while(j<mCols):
        if j%2==1 :
            i=i-1
        else:
            i=i+1
        while(0<=i and i<nRows):
            print(mat[i][j],end=' ')
            if(j%2==1):
                i=i-1
            else:
                i=i+1
        j=j+1
    print()



#Taking Iput Using Fast I/O

def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
