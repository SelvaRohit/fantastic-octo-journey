class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_int_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        index=0
        integer=[]
        # Roman_int_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # for index,Roman in enumerate(Roman_int_dict):
        # 

        # print("112")
        # Roman_int_length = len(s)
        for index,current_letter in enumerate(s):
            if(not integer):
                integer.append(Roman_int_dict[current_letter])
            elif(integer[-1] < Roman_int_dict[current_letter]):
                integer[-1] = - integer[-1]
                integer.append(Roman_int_dict[current_letter])
            else:
                integer.append(Roman_int_dict[current_letter])
        return (sum(integer))
obj=Solution()
print(obj.romanToInt('XC'))
                
                    
                        
                
