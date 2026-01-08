class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        Use Binary Search to keep on find the element
        To index the element from matrix use the special formula
        """
        rows=len(matrix)
        cols=len(matrix[0])
        start=0
        end=rows+cols
        mid=((end-start)//2)+1
        mid_row_index=mid//cols
        mid_col_index=mid%cols
