class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start=intervals[0][1]
        end=intervals[0][1]
        merged=[None,None]
        answer=[]
        for cur_start, cur_end in intervals[1:]:
            if cur_start>=end:
                merged=[start,cur_end]
                end=cur_end
            else:
                if merged[0] !=None:
                    start=cur_start
                    end=cur_end
                    answer.append(merged)
                    merged=[None,None]


            


