nums = [1, 2, 3, 4]

prefix = [1] * len(nums)
suffix = [1] * len(nums)
result = [1] * len(nums)
'''
for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] * nums[i-1]

for j in range(len(nums)-2,-1,-1):
    suffix[j] = suffix[j + 1] * nums[j+1]

print(prefix)
print(suffix)

for k in range(0,len(nums)):
    result[k] = prefix[k] * suffix[k]

print(result)
'''
#优化版
def productExceptSelf(nums):
    answer = [1] * len(nums)
    right_product = 1
    # 第一遍：从左往右
    # 让 answer[i] 保存 nums[i] 左边所有数的乘积
    for i in range(1,len(nums)):
        answer[i] = answer[i-1] * nums[i-1] 
    # 第二遍：从右往左
    for j in range(len(nums)-1,-1,-1):
    # 用一个 right_product 保存右侧乘积
        answer[j] *= right_product
        right_product *= nums[j]


    return answer

print(productExceptSelf(nums))