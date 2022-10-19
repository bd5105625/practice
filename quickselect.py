nums = [3, 17, -5, 4, 13, 8, 7, 6, 9]

# def change():
#     nums[0],nums[1] = nums[1],nums[0]


def partition(l,r):
    # pivot = nums[l]
    # i = l+1
    pivot = nums[r]
    i = l
    for j in range(l,r):

        if nums[j] <= pivot:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    nums[i],nums[r] = nums[r],nums[i]
    return i

def kthsmallest(l,r,k):

    if k > 0 and k <= r-l+1:
        index = partition(l,r)

        if index - l == k-1:
            return nums[index]

        if index-l > k - 1:
            return kthsmallest(l,index-1,k)
        
        if index-l < k - 1:
            return kthsmallest(index+1,r,k-(index-l+1))
print(nums)
print(kthsmallest(0,len(nums)-1,8))
print(nums)




# def qselect(arr,N,k):
#     lo = 0
#     hi = N-1
#     while(hi>lo):
#         m = qspart(arr,lo,hi)
#         print('m=',m)
#         if m == k: 
#             print('final',m)
#             return arr[m]
#         if m < k: lo = m+1
#         else: hi = m-1
#     # print('k',m,k)
#     return arr[k]

# def qspart(arr,lo,hi):
#     i = lo+1
#     j = hi
#     while True:
#         while arr[i] < arr[lo]:
#             # print(i)
#             i += 1
#             if i == hi: break
#         while arr[lo] < arr[j]:
#             j -= 1
#             if j == lo: break
#         if i >= j: break
#         arr[i],arr[j] = arr[j],arr[i]
#         print(arr)
#     arr[lo],arr[j] = arr[j],arr[lo]
#     print(arr)
#     return j 

# # nums = [3, 17, -5, 4, 13, 8, 7, 6, 9]
# nums = [9, 8, 6, 4, -100]
# # nums = [2,1,9,5,7,0,4]
# print(nums)
# k = 3
# print(qselect(nums,len(nums),4))

