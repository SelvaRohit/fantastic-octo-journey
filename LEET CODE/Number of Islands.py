class Solution(object):
    def dfs(self,row_index,col_index):
            top,bottom,left,right=row_index-1,row_index+1,col_index-1,col_index+1
            if 0<=top<=self.grid_rows and 0<=col_index<=self.grid_cols and self.grid[top][col_index]=='1':
                self.grid[top][col_index]='0'
                self.dfs(row_index=top,col_index=col_index)
                # pass
            if 0<=bottom<=self.grid_rows and 0<=col_index<=self.grid_cols and self.grid[bottom][col_index]=='1':
                self.grid[bottom][col_index]='0'
                self.dfs(row_index=bottom,col_index=col_index)
                # pass
            if 0<=row_index<=self.grid_rows and 0<=left<=self.grid_cols and self.grid[row_index][left]=='1':
                self.grid[row_index][left]='0'
                self.dfs(row_index=row_index,col_index=left)
                # pass
            if 0<=row_index<=self.grid_rows and 0<=right<=self.grid_cols and self.grid[row_index][right]=='1':
                self.grid[row_index][right]='0'
                self.dfs(row_index=row_index,col_index=right)
                # pass
            # pass
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.numOfIslands=0
        self.grid=grid
        self.grid_rows,self.grid_cols=len(grid)-1,len(grid[0])-1
        # @staticmethod
        for row_index,row in enumerate(grid):
            for col_index,element in enumerate(row):
                if element =='1':
                    self.numOfIslands+=1
                    grid[row_index][col_index]='0'
                    self.dfs(row_index=row_index,col_index=col_index)
        return self.numOfIslands

if __name__=='__main__':
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    obj=Solution()
    ans=obj.numIslands(grid=grid)
    print(ans)