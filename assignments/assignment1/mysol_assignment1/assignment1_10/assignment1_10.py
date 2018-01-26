from functools import reduce
import time

class SizeError(BaseException):
    pass

class Matrix(object):
    def __init__(self, M):
        if len(M) == 0 or len(M[0]) == 0:
            raise SizeError('The size of matrix cannot be 0')
        self.M = M
        self.rsize = len(M)
        self.csize = len(M[0])

    def size_equal(self, other):
        return self.rsize == other.rsize and self.csize == other.csize

    def __add__(self, other):
        if not self.size_equal(other):        
            raise SizeError('The size of two matrix is not equal.')
        return self.__class__([[self.M[i][j] + other.M[i][j] \
                for j in range(self.csize)] for i in range(self.rsize)])
    
    def __sub__(self, other):
        if not self.size_equal(other):        
            raise SizeError('The size of two matrix is not equal.')
        return self.__class__([[self.M[i][j] - other.M[i][j] \
                for j in range(self.csize)] for i in range(self.rsize)])

    def __str__(self):
        return str(self.M)

    def slice(self, ri, rj, ci, cj):
        if ri < 0 or ci < 0 or rj > self.rsize or cj > self.csize:
            raise IndexError('slice index out of matrix bound')
        return self.__class__([[self.M[i][j] for j in range(ci, cj)]\
                for i in range(ri, rj)])
    
    def divide(self):
        M11 = self.slice(0, self.rsize>>1, 0, self.csize>>1)
        M12 = self.slice(0, self.rsize>>1, self.csize>>1, self.csize)
        M21 = self.slice(self.rsize>>1, self.rsize, 0, self.csize>>1)
        M22 = self.slice(self.rsize>>1, self.rsize, self.csize>>1, self.csize)
        return M11, M12, M21, M22

    def combine(self, C11, C12, C21, C22):
        C = []
        for i in range(C11.rsize):
            C.append([C11.M[i][j] for j in range(C11.csize)] \
                    + [C12.M[i][j] for j in range(C12.csize)])
        for i in range(C21.rsize):
            C.append([C21.M[i][j] for j in range(C21.csize)] \
                    + [C22.M[i][j] for j in range(C22.csize)])
        return self.__class__(C)

    __repr__ = __str__
        

class GSMatrix(Matrix):
    def __mul__(self, other):
        if self.csize != other.rsize:
            raise SizeError('The columns of A is not equal to the rows of B')
        if self.rsize == 1:
            r = [reduce(lambda x, y: x+y, [self.M[0][i] * other.M[i][j] \
                    for i in range(self.csize)]) for j in range(other.csize)]
            return self.__class__([r])
        if self.csize == 1:
            return self.__class__([[self.M[i][0] * other.M[0][j] \
                    for j in range(other.csize)] for i in range(self.rsize)])
        if other.csize == 1:
            r = [[reduce(lambda x, y: x+y, [self.M[i][j] * other.M[j][0] \
                    for j in range(self.csize)])] for i in range(other.rsize)]
            return self.__class__(r)

        A11, A12, A21, A22 = self.divide()
        B11, B12, B21, B22 = other.divide()
        C11 = (A11 * B11) + (A12 * B21)
        C12 = (A11 * B12) + (A12 * B22)
        C21 = (A21 * B11) + (A22 * B21)
        C22 = (A21 * B12) + (A22 * B22)
        
        return self.combine(C11, C12, C21, C22)


class SSMatrix(Matrix):
    def __init__(self, M):
        n = len(M)
        if n & (n -1) != 0:
            raise SizeError('The size of M must be 2^k (k >= 0)')
        super(SSMatrix, self).__init__(M)

    def __mul__(self, other):
        if self.csize != other.rsize:
            raise SizeError('The columns of A is not equal to the rows of B')
        if self.rsize == 1:
            r = [reduce(lambda x, y: x+y, [self.M[0][i] * other.M[i][j] \
                    for i in range(self.csize)]) for j in range(other.csize)]
            return self.__class__([r])
        if self.csize == 1:
            return self.__class__([[self.M[i][0] * other.M[0][j] \
                    for j in range(other.csize)] for i in range(self.rsize)])
        if other.csize == 1:
            r = [[reduce(lambda x, y: x+y, [self.M[i][j] * other.M[j][0] \
                    for j in range(self.csize)])] for i in range(other.rsize)]
            return self.__class__(r)
        
        A11, A12, A21, A22 = self.divide()
        B11, B12, B21, B22 = other.divide()
        P1 = A11 * (B12 - B22)
        P2 = (A11 + A12) * B22
        P3 = (A21 + A22) * B11
        P4 = A22 * (B21 - B11)
        P5 = (A11 + A22) * (B11 + B22)
        P6 = (A12 - A22) * (B21 + B22)
        P7 = (A11 - A21) * (B11 + B12)

        C11 = P4 + P5 + P6 - P2
        C12 = P1 + P2
        C21 = P3 + P4
        C22 = P1 + P5 - P3 - P7

        return self.combine(C11, C12, C21, C22)


def __test():
    A = B = []
    with open('assignment1_10.in') as fin:
        for line in fin:
            if line.strip() == '':
                break
                A.append(list(map(int, line.strip().split())))
        for line in fin:
            B.append(list(map(int, line.strip().split())))

        # test for grade-school algorithm
        GSA = GSMatrix(A[:])
        GSB = GSMatrix(B[:])
        start_gs = time.clock()
        GSC = GSA * GSB
        end_gs = time.clock()

        # test for strassen algorithm
        SSA = SSMatrix(A[:])
        SSB = SSMatrix(B[:])
        start_ss = time.clock()
        SSC = SSA * SSB
        end_ss = time.clock()

        print('The time of grade school algorithm: %f s' % (end_gs - start_gs))
        print('The time of strassen algorithm: %f s' % (end_ss - start_ss))

        # output result matrix
        with open('assignment1_10.out', 'w') as fout:
            for j in range(GSC.rsize):
                print(' '.join([str(GSC.M[i]) for i in range(GSC.csize)]), file=fout)
                    

if __name__ == '__main__':
    __test()
