class Matrix:

    def unit_matrix(self,n):
        return [[0]*i+[1]+[0]*(5-i-1) for i in range(n)]

    def zero_matrix(self,n,m):
        return [[0]*m for _ in range(n)]

    def LUdecomposition(self,matA):
        n=len(matA)
        L=self.zero_matrix(n,n)
        U=self.unit_matrix(n)
        
        for i in range(n):
            for j in range(i+1):
                l=matA[i][j]
                for k in range(j): l-=L[i][k]*U[k][j]
                L[i][j]=l
            for j in range(i+1,n):
                u=matA[i][j]
                for k in range(i): u-=L[i][k]*U[k][j]
                U[i][j]=u/L[i][i]
        return L,U

    def matrix_calc(self,matA,matB,op):
        n,m=len(matA),len(matA[0])
        if len(matA)!=len(matB) or len(matA[0])!=len(matB[0]): return TypeError
        for i in range(n):
            for j in range(m):
                matA[i][j]=eval(str(matA[i][j])+op+str(matB[i][j]))
        return matA

    def matrix_dot(self,matA,matB):
        na,ma=len(matA),len(matA[0])
        nb,mb=len(matB),len(matB[0])
        if (ma!=nb): return ValueError
        res=[[0]*mb for _ in range(na)]
        for i in range(na):
            for j in range(mb):
                for k in range(ma):
                    res[i][j]+=matA[i][k]*matB[k][j]
        return res

    def matrix_det(self,matA):
        if len(matA)!=len(matA[0]): return ValueError
        L,U=self.LUdecomposition(matA)
        res=1
        for i in range(len(matA)): res*=L[i][i]
        return res

    def inverse_matrix(self,matA):
        detL,detU=self.LUdecomposition(matA)
        n=len(matA)
        for i in range(n):
            detL[i][i]=1/detL[i][i]
            detU[i][i]=1/detU[i][i]
        return self.matrix_dot(detL,detU)