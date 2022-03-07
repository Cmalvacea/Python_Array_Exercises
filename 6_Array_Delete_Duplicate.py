nums = [0,0,1,1,1,2,2,3,3,4]
nums2 = [1,1,2]

 
i=0
def RemoveDuplicates():
    while(i<len(nums)):    
        if nums.count(nums[i])>1:
            nums.remove(nums[i])
            i=i-1    
    i=i+1  
    k=len(nums)
    return k