class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict={}
        for _ in t: 
            t_dict[_]=t_dict.get(_,0) + 1
        print(t_dict)
        t_dict_copy=t_dict.copy()
        s_dict={}
        ans=''
        t_len=len(t)
        left=0
        right=0
        ans_found=False 
        try:
            if len(s)>=len(t):
                while(left<=len(s)-len(t) and right<=len(s)):
                    if not ans_found:
                        curr_char=s[right]
                        if curr_char in t_dict:
                            s_dict[curr_char]=s_dict.get(curr_char,0) + 1
                        # else:
                        #     left+=1
                        if s_dict == t_dict:
                            # ans=s[left:right+1]
                            ans_found=True
                        right+=1
                    else: #Once the left to right index have the string t.
                        remove_char=s[left]
                        if remove_char not in s_dict:
                            left+=1
                            ans=s[left:right]
                        else:
                            if (len(ans)==0 or len(ans)>len(s[left:right])):
                                ans=s[left:right]
                            left=right
                            ans_found=False
                            s_dict={}

            return ans
        except IndexError:
            return ans



if __name__=='__main__':
    s='ADOBECODEBANC'
    t='ABC'
    s='bdab' #139th case
    t='ab'
    obj=Solution()
    a=obj.minWindow(s,t)
    print(a)