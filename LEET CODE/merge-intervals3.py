class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        This logic will work, if the intervals are sorted
        w.r.t start index (i)
        """
        if len(intervals) ==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        start=intervals[0][0]
        end=intervals[0][1]
        merged=[None,None]
        answer=[intervals[0]]
        for cur_start, cur_end in intervals[1:]:
            if cur_start<=end:
                if cur_end>=answer[-1][1]:
                    answer[-1][1]=cur_end
                if cur_start<=answer[-1][0]:
                    answer[-1][0]=cur_start
                end=cur_end
            else:
                answer.append([cur_start,cur_end])
        return answer
if __name__ == "__main__":
    obj = Solution()
    arr=[[1,3],[2,6],[8,10],[15,18]]
    arr1=[[1,4],[4,5]]
    arr2=[[1,4],[0,4]]
    arr3=[[1,4],[0,0]]
    arr4=[[2,3],[4,5],[6,7],[8,9],[1,10]]
    print(obj.merge(arr4))

            


