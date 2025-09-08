class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i=0
        j=1
        merge=False
        start=None
        answer=[]
        while i< len(intervals):
            if j<len(intervals):
                if intervals[i][1] >= intervals[j][0]:
                    start=i
                    i=j
                    j+=1
                    merge=True
                elif intervals[i][1] < intervals[j][0]:
                    if merge:
                        answer.append([intervals[start][0],intervals[i][1]])
                        i=j
                        j=i+1
                    else:
                        answer.append(intervals[i])
                        i=j
                        j=i+1
                    merge=False
                    start=None
                    
                # else:
            else:
                if merge:
                    pass
        return answer
if __name__ == "__main__":
    obj = Solution()
    arr=[[1,3],[2,6],[8,10],[15,18]]
    print(obj.merge(arr))




