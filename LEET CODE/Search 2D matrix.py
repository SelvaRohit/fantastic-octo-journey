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
        end=(rows*cols)-1
        while start <= end:
            mid=((end+1-start)//2)+start
            mid_row_index=mid//cols
            mid_col_index=mid%cols
            to_check=matrix[mid_row_index][mid_col_index]
            if  to_check== target:
                return True
            elif to_check > target:
                # start=0
                end=mid-1
            else:
                start=mid+1
                # end=rows*cols
            # print(start,end)
        return False


if __name__ == "__main__":
    obj=Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 10
    out=obj.searchMatrix(matrix=matrix,target=target)
    print(out)