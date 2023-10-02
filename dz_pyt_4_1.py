# Функция транспонирования матрицы
def tran(matr):
    res=[]
    n=len(matr)
    m=len(matr[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp+=[matr[i][j]]
        res+=[tmp]
    return res
mat = [[1, 2], [3, 4], [5, 6]]
print(tran(mat))
