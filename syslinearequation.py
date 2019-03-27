# matrix shape
def shape(m):
    row_sizes = []
    for i in range(len(m)):
        row_sizes.append(len(m[i]))

    if not isinstance(m, list):
        print('Error: Input must be in a list format.')
    elif len(set(row_sizes)) == 1:
        row_size = len(m)
        column_size = len(m[0])
        return row_size, column_size
    else:
        print('Error: Matrix rows are not uniform in size.')

# matrix transpose
def transpose(m):
    row_sizes = []
    trans_list = []
    for i in range(len(m)):
        row_sizes.append(len(m[i]))

    if not isinstance(m, list):
        print('Error: Input must be in a list format.')
    elif len(set(row_sizes)) == 1:
        result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        for row in result:
            trans_list.append(row)
        return trans_list
    else:
        print('Error: Matrix rows are not uniform in size.')


def list2mul(m):
    ls = []
    k = 1

    for i in m:
        for j in i:
            k = k * j
        ls.append(k)
        k = 1

    return ls

def listadd(m):
    k = 0
    for i in m:
        k = k + i

    return k

def det(A):
    rowsize, colsize = shape(A)

    if rowsize == 2 and colsize == 2:
        return det2(A)
    elif rowsize == 3 and colsize == 3:
        return det3(A)
    else:
        print('Error: Input should be a square matrix.')

# determinant of 2x2 matrix
def det2(A):
    return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

# determinant of 3x3 matrix
def det3(A):
    B = []
    C = []
    A1, A2 = [], []

    rowsize, colsize = shape(A)

    for i in A:
        tmp = []
        for j in range(colsize-1):
            tmp.append(i[j])
        B.append(tmp)

    for i,j in zip(A,B):
        C.append(i+j)

    start1, start2 = 0, colsize-1
    stop1, stop2 = colsize, start2+colsize

    for i in C:
        A1.append(i[start1:stop1])
        start1 += 1
        stop1 += 1

    for i in C:
        A2.append(i[start2:stop2])
        start2 -= 1
        stop2 -= 1

    n1 = listadd(list2mul(transpose(A1)))
    n2 = listadd(list2mul(transpose(A2)))

    det = n1-n2

    return det
