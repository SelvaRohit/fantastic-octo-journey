class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)): #Replacing 0 with 'a'
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    matrix[0][col]='a'
                    matrix[row][0]='a'
        for col in range(1,len(matrix[0])):
            if matrix[0][col]=='a':
                for row in range(len(matrix)):
                    matrix[row][col]=0
        for row in range(1,len(matrix)):
            if matrix[row][0] =='a':
                for col in range(len(matrix[0])):
                    matrix[row][col]=0
        if matrix[0][0]=='a':
            for row in range(len(matrix)):
                matrix[row][0]=0
            for col in range(len(matrix[0])):
                matrix[0][col]=0
if __name__ == "__main__":
    obj = Solution()
    mat=[[1,1,1],[1,0,1],[1,1,1]]
    mat1=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    mat3=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    obj.setZeroes(mat3)
    print(mat3)