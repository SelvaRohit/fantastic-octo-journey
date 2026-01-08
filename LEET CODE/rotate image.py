class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix_len=len(matrix)
        temp=[matrix[_][:] for _ in range(matrix_len)]
        start,end=0,0
        for i in range(matrix_len):
            for j in range(matrix_len-1,-1,-1):
                matrix[start][end]=temp[j][i]
                end+=1
            end=0
            start+=1
        # print(matrix)
        # matrix=temp
            




if __name__=='__main__':
    matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    output=[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    # print(len(matrix))
    # print([[0]*4 for _ in range(4)])
    obj=Solution()
    obj.rotate(matrix=matrix)
