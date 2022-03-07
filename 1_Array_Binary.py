count = 0
maxc=0
nums = [0,1,0,1,1,1]
for x in nums:
    if x==1:
        count+=1
        if count > maxc:
            maxc = count
            print(maxc)
    else:
        count=0
