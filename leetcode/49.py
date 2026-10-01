def groupAnagrams(strs):
    groups = {}

    for word in strs:
        # 1. 创建长度 26 的 count
        count = [0] * 26
        # 2. 遍历 word，统计字母
        for c in word:
            x = ord(c) - ord('a')
            count[x] += 1
        # 3. count 转 tuple 得到 key
        y = tuple(count)
        # 4. 把 word 放进 groups[key]
        groups[y] = groups.get(y,[])
        groups[y].append(word)
    # 5. 返回 groups 里面所有的 value
    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))