from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        print(s)
        total += s.shares * s.price
    return total

print(compute_cost([('a', 1, 20), ('a', 3, 20)]))

# nametuple是一个工厂方法,返回一个类
a = Stock([1,2,3], tuple, list)  # 初始化化这个类
b = Stock(2,3,4)
print(a)
print(b)
c = a._replace(name=56)
print(c)
print(a)
