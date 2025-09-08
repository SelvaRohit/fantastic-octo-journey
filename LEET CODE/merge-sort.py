l12=[1,5,2,5,1,6,3,9,45,8]
# l12=[1,5,2]
def merge_sort(arr,l,r):
    if l<r:
        mid=(l+r)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)
def merge(arr,l,mid,r):
    n1=(mid-l+1)
    n2=(r-mid)
    l1=[0]*n1
    l2=[0]*n2
    for i in range(n1):
        l1[i]=arr[l+i]
    for j in range(n2):
        l2[j]=arr[mid+1+j]
    i=0
    j=0
    k=l
    b=[0]*(n1+n2)
    while i<n1 and j<n2:
        if l1[i] < l2[j]:
            arr[k]=l1[i]
            i+=1
        else:
            arr[k]=l2[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=l1[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=l2[j]
        j+=1
        k+=1
merge_sort(l12,0,len(l12)-1)
print(l12)
