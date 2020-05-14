# """Find the k largest values in an array of n numbers."""
# """Return them in a new array sorted in decreasing order."""
# def kLargest(nums, k): 
#     # Sort the given array arr in reverse order.   
#     nums.sort(reverse = True) 
#     # Print the first kth largest elements 
#     for i in range(k): 
#         print (nums[i], end =" ")  
  

# nums1 = [1, 23, 12, 9, 30, 2, 50] 
# nums = [5,10,15,20,25,30]

# k = 3
# kLargest(nums1, k)
# kLargest(nums, k)  

"""Given an array a of numbers and a target value t, find"""
"""two numbers that sum to t (that is, a[i] + a[j] = t)."""
def two_sum(arr, t):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == t:
                return (arr[i], arr[j])
            
t = 5
arr = [5,2,5,3,8]
print(two_sum(arr, t))

#time complexity is o(n^2) because of the nested for loop
