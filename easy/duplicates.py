
nums = [2,2,3,4,5,2,6,7,8]

nums = sorted(nums)
count = 0 
print(f" before: {nums}")

for i in range(len(nums) - 1):
    if nums[i + 1] == nums[i]:
        count += 1

del nums[:count]

print(nums)