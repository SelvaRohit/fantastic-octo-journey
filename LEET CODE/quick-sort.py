inp=[1,3,5,2,0,5,3,8,1]
def partition(arr,lb,ub):
    pivot=arr[lb]
    start=lb
    end=ub
    while (start<end):
        while (arr[start]<=pivot):
            start+=1
        while (arr[end]>pivot):
            end-=1
        if (start<end):
            arr[start],arr[end]=arr[end],arr[start]
    arr[end]=arr[lb]
    return end
def quick_sort(arr,lb,ub):
    if lb<ub:
        pi=partition(arr,lb,ub)
        quick_sort(arr,lb,pi-1)
        quick_sort(arr,pi+1,ub)
quick_sort(inp,0,len(inp)-1)
print(inp)
