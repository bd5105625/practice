


# def qspart(a,lo,hi):
#     i = lo
#     j = hi+1
#     while True:


# def qsort_h(a,lo,hi):
#     if hi <= lo:
#         return ;
#     mid = qspart(a,lo,hi)



def qspart(arr,lo,hi):
    i = lo
    j = hi+1

    temp_sorted = sorted(arr[lo:hi])
    value = temp_sorted[(hi-lo+1)//5-1]
    index = arr[lo:hi].index(temp_sorted[(hi-lo+1)//5-1])
    if index < lo: index = lo
    arr[index],arr[lo] = arr[lo],arr[index]
    pivot = arr[lo]
    
    while True:
        # i+=1
        while True:
            i+=1
            if arr[i] > pivot:
                break
            if i == hi: break
        while True:
            j -= 1
            if pivot > arr[j]:
                break
            if j == lo:
                break

        if i >= j: break
        arr[i],arr[j] = arr[j],arr[i]
    arr[lo],arr[j] = arr[j],arr[lo]
    return j 


def qsort_h(a,lo,hi):
    if hi <= lo:
        return
    mid = qspart(a,lo,hi)
    qsort_h(a,lo,mid-1)
    qsort_h(a,mid+1,hi)

nums = [1, 3, -5, -2, 0, 1000, 4, 7, 10, 15, 11]

qsort_h(nums,0,len(nums)-1)
print(nums)