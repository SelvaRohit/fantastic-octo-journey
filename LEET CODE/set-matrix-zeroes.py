class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        cols=set()
        # rows.add(1)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in cols:
            for j in range(len(matrix)):
                matrix[j][i]=0
if __name__ == "__main__":
    obj = Solution()
    mat=[[1,1,1],[1,0,1],[1,1,1]]
    mat1=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    obj.setZeroes(mat1)
    print(mat1)
        
        