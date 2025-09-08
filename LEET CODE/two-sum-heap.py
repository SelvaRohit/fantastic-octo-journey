numbers=[3,2,3]
target=6
heap={}
for i,element in enumerate(numbers):
    if heap.get(element) != None:
        print([heap[element],i])
    else:
        found=target-element
        heap.update({found:i})