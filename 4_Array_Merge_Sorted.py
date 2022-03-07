nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = len(nums2)

#Output [1,2,2,3,5,6]

def MergeSorted():
    for i in nums2:
        nums1.insert(0,i)
        nums1.pop()
    nums1.sort()
    print(nums1)


MergeSorted()
