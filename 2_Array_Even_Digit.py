nums = [555,901,482,1771]
total = 0

nums.sort()

for num in nums:
    digit = str(num)
    if len(digit) % 2 == 0:
        total += 1
        print(num)

