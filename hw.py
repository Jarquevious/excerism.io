def dna_comparison(arr, nums):
    count = 0
    for i, j in zip(nums, arr):
        if i != j:
            count += 1
    return count 

        
# arr = 'GAGCCTACTAACGGGAT'
# nums = 'CATCGTAATGACGGCCT'
# print(dna_comparison(arr, nums))

# edge cases
# arr1 = 'zdfgnghxnhgxn'
# nums1 = 'xvbgf'
# print(dna_comparison(arr1, nums1))

arr2 = ''
nums2 = 'jarquevious'
print(dna_comparison(arr2, nums2))

arr3 = 'JARQUEVIOUS'
nums3 = 'jarquevious'
print(dna_comparison(arr3, nums3))