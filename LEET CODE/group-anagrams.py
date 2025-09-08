from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d1=defaultdict(list)
        for i in strs:
            sorted_key=''.join(sorted(i))
            d1[sorted_key].append(i)
        return list(d1.values())
if __name__ == "__main__":
    obj = Solution()
    arr=["eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(arr))
        
if __name__ == "__main__":
    obj = Solution()
    arr=["eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(arr))        