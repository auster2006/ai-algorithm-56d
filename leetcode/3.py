def lengthOfLongestSubstring(s):
    l = r = 0
    window = set()
    max_length = 0
    while r < len(s):

        # 如果新来的 s[r] 重复了
        while s[r] in window:
            window.remove(s[l])
            l += 1

        # 现在 s[r] 已经不重复
        window.add(s[r])

        # 当前合法窗口长度
        max_length = max(max_length, r - l + 1)

        # 右边界继续走
        r += 1

    return max_length