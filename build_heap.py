def heapify(arr,N,i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    print(arr)
    # If left child is larger than root
    if l < N and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < N and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        heapify(arr, N, largest)
    

def buildHeap(arr, N):
    # Index of last non-leaf node
    startIdx = N // 2 - 1
    for i in range(startIdx, -1, -1):
        print(arr[i])
        heapify(arr, N, i)
        # print(arr)
    
 

# a = [4,2,7,9,12,1,3,0,10,11]
a = [2, 11, 7, 10, 4, 1, 3, 0, 9]
buildHeap(a,len(a))
print(a)