# A
# 建立一个字典：
# apple -> 5
# banana -> 8
# orange -> 3
#
# 遍历并打印数量 >= 5 的水果
fruits = {
    "apple":5,
    "banana":8,
    "orange":3
}

for name,num in fruits.items():
    if num >= 5:
        print(name,num)

# B
x = [1, 1, 2, 3, 3, 4]
y = [3, 4, 4, 5]

# 用 set 得到：
# x 去重
# x 和 y 的交集
# x 和 y 的并集
X = set(x)
Y = set(y)
print(X)
print(X & Y)
print(X | Y)


# C
nums = [1, 2, 3, 4, 5, 6]

# 一行列表推导式：
# 得到其中所有奇数的平方
new_nums = [k ** 2 for k in nums if k % 2 == 1]

# D
# 创建 Rectangle 类
# 属性：
# width
# height
#
# 方法：
# area()
# 返回 width * height
#
# 最后创建：
# Rectangle(3, 5)
# 并打印面积

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(3, 5)

print(r.area())
    
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return(3.14 * self.radius ** 2)

c = Circle(5)

print(c.radius) 
print(c.area())
        