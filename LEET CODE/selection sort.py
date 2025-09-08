""" Description: First choose the first element as minimum element and store
    the index as well then traverse the remaining element to find the most minimum
    element and their index till the end of the loop once loop ends you have the minimum
    element and their index swap that into the first index. Now you find the first element
    and do the same with second element as goes on."""
a=[2,5,7,3,2,9,1]
for i in range(len(a)-1):
    min_index=i
    min=a[i]
    for j in range(i+1,len(a)):
        if a[j]<=min:
            min=a[j]
            min_index=j
    a[i],a[min_index]=a[min_index],a[i]
print(a)
