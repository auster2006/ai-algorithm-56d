s = "A man, a plan, a canal: Panama"



def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        # 跳过左边无效字符
        while left < right and not s[left].isalnum():
            left += 1
        # 跳过右边无效字符
        while left < right and not s[right].isalnum():
            right -= 1
        # 比较左右有效字符
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False

    return True

print(isPalindrome(s))