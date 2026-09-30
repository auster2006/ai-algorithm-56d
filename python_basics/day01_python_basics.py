nums = [3, 7, 2, 9, 4, 7, 10, 3]
new_nums = [x^2 for x in nums if x >5]

scores = {
    "Alice": 82,
    "Bob": 95,
    "Charlie": 76,
    "David": 91
}
#不知道怎么调用字典里的值


a = [1, 2, 2, 3, 4, 4, 5]
b = [3, 4, 4, 5, 6, 7]
A = set(a)
B = set(b)
print(A,B)
print(A&B)
print(A|B)


def statistics(nums):
    a = max(nums)
    b = min(nums)
    c = sum(nums)/len(nums)
    return a,b,c

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

squares = [i ** 2 for i in nums if i % 2 == 0]