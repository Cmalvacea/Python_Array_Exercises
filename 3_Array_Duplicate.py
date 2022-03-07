arr = [1,0,2,3,0,4,5,0]

def DuplicateZero(arr):
    tdp = len(arr)
    i = 0
    while i < tdp:
        if arr[i]==0:
            arr.pop()
            arr.insert(i, 0)
            i += 2
        else:
            i += 1

DuplicateZero(arr)

print(arr)
        

