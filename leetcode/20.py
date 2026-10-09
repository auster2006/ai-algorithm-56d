def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        # 1. 如果是左括号，入栈
        if ch in {'(','[','{'}:
            stack.append(ch)
        # 2. 如果是右括号：
        if ch in {')',']','}'}:
            if not stack:
                return False
            if pairs[ch] == stack[-1]:
                stack.pop()
                continue
            else:
                return False
        #    检查栈是否为空
        #    检查栈顶是否匹配
        #    匹配成功就弹出栈顶
    if len(stack) > 0:
        return False

    return True
    # 3. 遍历结束后，判断栈是否为空