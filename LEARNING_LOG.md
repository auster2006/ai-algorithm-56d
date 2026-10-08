AI Algorithm 56-Day Learning Log

目标：系统掌握 Python、机器学习、深度学习、数理统计和算法基础，为 AI 算法实习做准备。

记录原则：每天记录学习内容、关键知识点、代码实践和复习重点。

Day 1 — Python 基础与 NumPy 入门

Python

字典 dict、集合 set、列表与推导式

enumerate()、类的基础概念

字典计数、集合去重

时间复杂度的基本分析

NumPy

数组创建、索引、矩阵运算

Broadcasting（广播机制）

X @ W + b 的含义

LeetCode



Two Sum：哈希表，O(n)



Contains Duplicate：集合去重，O(n)

复习重点

字典和集合的区别

为什么哈希表能优化查找

NumPy 广播规则

Day 2 — 线性回归与概率模拟

机器学习

线性模型 y = wx + b

均方误差 MSE

梯度下降 Gradient Descent

学习率对收敛的影响

最小二乘法 np.linalg.lstsq()

NumPy 实践

随机生成带噪声的数据

手动计算梯度并更新参数

比较梯度下降与最小二乘解

概率统计

Bernoulli、Binomial、Normal、Poisson 分布

样本均值与样本方差

使用 NumPy 模拟随机变量

LeetCode

242. Valid Anagram：字典计数



Group Anagrams：字符频率向量作为哈希键

复习重点

MSE 梯度如何推导

学习率过大或过小的后果

为什么字典的键可以使用 tuple

Day 3 — PyTorch 与自动求导

PyTorch

Tensor 创建、索引与形状

CPU/GPU 设备管理

.to("cuda")

requires_grad

backward() 与 .grad

torch.no_grad()

梯度清零 zero_()

机器学习实践

用 PyTorch 实现线性回归

利用 autograd 自动计算梯度

理解训练循环中的参数更新

概率统计

Poisson 分布

Markov 性质相关练习

算法

347. Top K Frequent Elements：桶排序思路（练习及后续复习）

复习重点

计算图与链式法则

为什么梯度会累积

为什么参数更新时通常不记录梯度

Day 4 — 梯度、条件概率与蒙特卡洛

PyTorch / 数学

矩阵运算中的梯度

自动求导与手动求导对照

概率统计

条件概率与贝叶斯公式

条件期望

Monte Carlo 模拟

LeetCode

36. Valid Sudoku：哈希集合



Longest Consecutive Sequence：集合与连续序列起点

复习重点

条件概率和条件期望的区别

Monte Carlo 的基本思想

如何利用集合避免重复遍历连续序列

Day 5 — 神经网络基础

PyTorch

nn.Module

nn.Linear

nn.MSELoss

torch.optim.SGD

forward()

标准训练循环

多层感知机 MLP

ReLU 激活函数

概率统计

Poisson 分布

Exponential 分布及其关系

LeetCode

125. Valid Palindrome：双指针



Two Sum II：有序数组双指针

复习重点

nn.Module 与普通 Python 类的关系

线性层和激活函数分别做什么

zero_grad → forward → loss → backward → step

Day 6 — Pandas、SQL 与双指针

Pandas

DataFrame 与 Series

读取和分析 Titanic 数据

groupby()

merge()

数据筛选、聚合

SQL

SELECT、WHERE

GROUP BY

JOIN

聚合函数

LeetCode

15. 3Sum：排序 + 双指针 + 去重



Container With Most Water：双指针

复习重点

Pandas groupby 的聚合逻辑

SQL JOIN 的基本区别

双指针为什么能减少搜索空间

Day 7 — 第一周复习

综合复习

Python、NumPy、PyTorch

概率分布与条件概率

已学算法题型整理

LeetCode

121. Best Time to Buy and Sell Stock：维护历史最低价



Longest Substring Without Repeating Characters：滑动窗口

复习重点

滑动窗口左右指针如何移动

哈希表如何记录窗口状态

最大利润与历史最低价的关系

Day 8 — 参数估计与滑动窗口

数理统计

极大似然估计 MLE

Bernoulli 参数估计

Normal 均值参数估计

无偏估计与一致估计

Bias、Variance、MSE

样本方差为什么除以 n−1

Monte Carlo 估计误差与 1/√n

LeetCode

424. Longest Repeating Character Replacement：可变长度滑动窗口



Permutation in String：固定长度滑动窗口



Top K Frequent Elements：桶排序复习

复习重点

MLE 如何从似然函数推导

无偏性与一致性的区别

固定窗口和可变窗口的区别

Day 9 — 线性回归、抽样分布与栈

机器学习

正态噪声假设下，最小二乘法与 MLE 的联系

np.linalg.lstsq()

sklearn.linear_model.LinearRegression

.fit()、.predict()

.coef_、.intercept_

reshape(-1, 1)

异常值对 MSE 和回归参数的影响

数理统计

总体标准差 σ 与样本标准差 S

自由度及 n−1 的来源

标准正态分布

卡方分布 χ²

Student t 分布

F 分布

样本均值与样本方差的抽样分布

t 分布与 F 分布的关系

Python

class 与对象

__init__ 的初始化作用

self 与实例属性

Python 列表模拟栈

append()、pop()、stack[-1]

LeetCode

20. Valid Parentheses：栈与括号匹配



Min Stack：双栈维护当前最小值



Best Time to Buy and Sell Stock：思路复习

复习重点

σ 与 S 的区别

正态、t、卡方、F 分布的识别

为什么 t 分布的自由度是 n−1

self 与普通局部变量的区别

为什么 Min Stack 需要保存历史最小值