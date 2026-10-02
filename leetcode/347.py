nums = [1,1,1,2,2,3]
k = 2

freq = {}

result = []

for x in nums:
    freq[x] = freq.get(x, 0) + 1

bucket = [[] for _ in range(len(nums) + 1)]

for num,fr in freq.items():
    bucket[fr].append(num)

k0 = 0
for i in range(len(nums),0,-1):
    if bucket[i] != []:
        k0 += len(bucket[i])
        result.extend(bucket[i])
        if k0 >= k:
            break

print(result[:k])