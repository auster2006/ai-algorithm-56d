def threeSum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        # 处理 i 的重复
        if i > 0 and nums[i] == nums[i-1]:
            continue


        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            # total < 0
            if total < 0:
                l += 1
            # total > 0
            elif total > 0:
                r -= 1
            else:
                ans.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            # total == 0

    return ans