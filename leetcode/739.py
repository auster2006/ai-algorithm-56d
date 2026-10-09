class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)

        # 每一天的等待天数，默认都是 0
        ans = [0] * n

        # 单调栈：存储日期下标
        stack = []

        for i in range(n):

            # TODO 1：什么条件下需要弹栈？
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # TODO 2：弹出栈顶日期
                j = stack.pop()

                # TODO 3：计算等待天数
                ans[j] = i-j

            # TODO 4：将当前日期入栈
            stack.append(i)

        return ans


# 测试
s = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(temperatures))