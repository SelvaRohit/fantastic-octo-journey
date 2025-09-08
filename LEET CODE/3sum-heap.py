nums=[1,2,3,-1,5,0]
target1=0
for j,fixed_element in enumerate(nums):
    heap={}
    target=target1-fixed_element
    temp=nums[j+1:]
    for i,element in enumerate(temp):
        if heap.get(element) != None:
            print([j,heap[element],i+j+1])
        else:
            found=target-element
            heap.update({found:i+1+j})