class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        numOfElements=len(matrix)+len(matrix[0])
        out=[]
        traversed=set()
        i=mode=0
        j=-1

        while len(out) < numOfElements:
            # if (i,j) not in traversed:
            #     mode=0
            # elif (i+1,j) not in traversed:
            #     i+=1
            #     mode=1
            # elif(i,j-1) not in traversed:
            #     j-=1
            #     mode=2
            # elif(i-1,j) not in traversed:
            #     i-=1
            #     mode=3
            # elif (i,j+1) not in traversed:
            #     j+=1
            #     mode=0

            while (i<len(matrix) and j<len(matrix[0])):
                if mode==0:
                    j+=1
                elif mode==1:
                    i+=1
                elif mode==2:
                    j-=1
                else:
                    i-=1
                if (i>=len(matrix)):
                    i-=1
                    break
                elif (j>=len(matrix[0])):
                    j-=1
                    break
                out.append(matrix[i][j])
                traversed.add((i,j))
            mode=(mode+1)%4
        return out
if __name__ == "__main__":
    obj = Solution()
    mat=[[1,2,3],[4,5,6],[7,8,9]]
    print(obj.spiralOrder(mat))
