nums = [100, 4, 200, 1, 3, 2]

num_set = set(nums)

max_length = 0

for x in num_set:
    if x - 1 not in num_set:
        # x 是起点

        current = x
        current_length = 1

        # while ...
            # current 往后走
            # length + 1
        while (current+1) in num_set:
            current += 1
            current_length += 1
        # 更新 max_length
        max_length = max(max_length,current_length)
print(max_length)