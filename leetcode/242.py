def isAnagram(s, t):
    dict_s = {}
    dict_t = {}
    for x in s:
        if x in dict_s:
            dict_s[x] += 1
        else:
            dict_s[x] = 1
        #dict_s[x] = sict_s.get(x,0) + 1
    for y in t:
        if y in dict_t:
            dict_t[y] += 1
        else:
            dict_t[y] = 1
    return dict_s == dict_t