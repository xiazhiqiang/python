#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = input("请输入名字：")
print("名字是：", name)

# ----------------------------------------------------------------

# r''表示''内部的字符串默认不转义
print(r"\\\\t")

print("%2d-%02d %%" % (3, 1))

"Hello, {0}, 成绩提升了 {1:.1f}".format("小明", 17.125)

a = 1
b = 1
f"echo {a} {b:.2f}"

# ----------------------------------------------------------------

list = ["Joe", "Jack", 111]
print(len(list))
list.append("Tom")
print(list)
list.pop(2)
print(list)
list.insert(1, "John")
print(list)
print("list 截取到索引2", list[:2])
list2 = list[:]
print("list2", list2)

# ----------------------------------------------------------------

t = (1, [2, 3])
t2 = (1,)
print(t, t2)
t[1][0] = 4
print(t, t2)

# ----------------------------------------------------------------

age = int(input("请输入年龄:"))
if age >= 18:
    print("已成年")
elif age >= 6:
    print("少年")
else:
    print("未成年")

list = []
if list:
    print("not empty list")
else:
    print("empty list")

t = ()
if t:
    print("not empty tuple")
else:
    print("empty tuple")

# ----------------------------------------------------------------

for item in [1, 2, 3]:
    print(item)
for index, value in enumerate([4, 5, 6]):
    print(index, value)

for value in (4, 5, 6):
    print(value)

idx = 0
list = range(3)
while idx < len(list):
    print(list[idx])
    idx = idx + 1

# ----------------------------------------------------------------

s = set([1, 1, 2, 2, 3, 4])
print(s)
s.add(1)
print(s)

# ----------------------------------------------------------------


def compare(a, b):
    inta = int(a)
    intb = int(b)
    if inta > intb:
        return 1
    elif inta < intb:
        return -1
    else:
        return 0


ret = compare(10, 20)
print("比较{0}与{1}".format(10, 20) + "的结果：", ret)


def nop():
    pass


print(nop())

import math


def quadratic(a, b, c):
    tmp1 = math.pow(b, 2) - 4 * a * c
    if tmp1 < 0:
        raise TypeError("方程无实根")
    else:
        return (-b + math.sqrt(tmp1)) / 2 * a, (-b - math.sqrt(tmp1)) / 2 * a


print(quadratic(2, 3, 1))


def f1(a, b, c=0, *args, **kw):
    print("a=", a, "b=", b, "c=", c, "args=", args, "kw=", kw)


f1(1, 2, 3, 99, d=10)
f1(*(1, 2, 3, 99), **{"d": 10})

# ----------------------------------------------------------------


# 查找列表中的最小值和最大值
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for value in L:
        if value > max:
            max = value
        if value < min:
            min = value
    return (min, max)


print(findMinAndMax([]) != (None, None))

# ----------------------------------------------------------------


def is_odd(value):
    return value % 2 == 1


print(filter(is_odd, range(1, 10)))

L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]
print(sorted(L, key=lambda t: t[1]))
print(sorted(L, key=lambda t: t[0]))


def createCounter():
    num = 0

    def counter():
        nonlocal num
        num = num + 1
        return num

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA())

# ----------------------------------------------------------------

import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = round(time.time() * 1000)
        result = fn(*args, **kwargs)
        end = round(time.time() * 1000)
        print("%s executed in %s ms" % (fn.__name__, end - start))
        return result

    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


print(fast(1, 2))

# ----------------------------------------------------------------

import mod

mod.hello()
