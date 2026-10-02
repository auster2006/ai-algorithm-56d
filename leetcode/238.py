nums = [1, 2, 3, 4]

prefix = [1] * len(nums)
suffix = [1] * len(nums)
result = [1] * len(nums)

for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] * nums[i-1]

for j in range(len(nums)-2,-1,-1):
    suffix[j] = suffix[j + 1] * nums[j+1]

print(prefix)
print(suffix)

for k in range(0,len(nums)):
    result[k] = prefix[k] * suffix[k]

print(result)