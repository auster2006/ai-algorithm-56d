def groupAnagrams(strs):
    answer = {}
    for x in strs:
        count = [0]*26
        for i in range(len(x)):
            count[ord(x[i])-ord("a")] += 1
        key = tuple(count)
        answer[key] = answer.get(key,[])
        answer[key].append(x)
    return list(answer.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

