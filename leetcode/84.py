class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # 1. 如果当前柱子更矮，不断弹栈
            while stack and heights[i] < heights[stack[-1]]:
            # 2. 计算弹出柱子对应的最大矩形面积
                top = stack.pop()
                left = stack[-1] if stack else -1
                area = (i - left - 1) * heights[top]
            # 3. 更新 max_area
                max_area = max(max_area,area)
            # 4. 将当前下标入栈
            stack.append(i)

        return max_area

heights = [2, 1, 5, 6, 2, 3]
# 预期输出：10
print(Solution().largestRectangleArea(heights))