import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        # 你的代码
        stack = []
        for x in tokens:
            if x in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                result = ops[x](a,b)
                stack.append(result)
            else:
                stack.append(int(x))

        return stack[0]


s = Solution()
tokens = ["4", "13", "5", "/", "+"]
print(s.evalRPN(tokens))