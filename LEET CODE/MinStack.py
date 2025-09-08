class MinStack(object):

    def __init__(self):
        self.arr=list()
        self.min_arr=list()
        self.min_val=None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.arr) ==0:
            self.min_val = val
            self.min_arr.insert(0,val)
        else:
            self.min_arr.insert(0,min(val,self.min_val))
            self.min_val= min(val,self.min_val)
        self.arr.insert(0,val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.arr:
            self.arr.pop(0)
            self.min_arr.pop(0)
            self.min_val= self.min_arr[0] if self.min_arr else None

    def top(self):
        """
        :rtype: int
        """ 
        if self.arr:
            return self.arr[0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_arr:
            return self.min_val
        

if __name__ == "__main__":
    # obj = Solution()sr
# Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(-3)
    obj.push(-11)
    # obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3,param_4)