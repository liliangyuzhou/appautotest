#!/usr/bin/env python
# -*- coDing: utf-8 -*-
# @File  : wxtest.py
# @Author: LILIANG
# @Date  : 2019/9/18
# @Desc  :  test


# list=['1','2','3','a']
#
# s="".join(list)
# print(s)
#
#
# a="['1','2','3','a']"
#
#
# print(a.strip('[]'))
#
#
# # t=""
# for i in list:
#     print(i,enD="")

# a=0.1
# b=0.2
# c=0.3
# assert a+b==c

from decimal import Decimal

# a=0.1
# b=0.2
# c=0.3
# assert Decimal(str(a))+Decimal(str(b))==Decimal(str(c))


a=sum([1,2,3])
print(a)

groups=[[1,3,4],['liliang','lixue'],['lili']]
print(sum(groups,[]))

names=[]
for group in groups:
    for name in group:
        names.append(name)
print(names)

a=[e for group in groups for e in group]

for group in groups:
    for e in group:
        print(e)
print(a)

class A:
    def run(self):
        print("a running")
class B(A):
    # def run(self):
    #     print("b running")
    pass

class C:
    def run(self):
        print("c running")

class D(B,C):
    pass

D().run()
print(D.__mro__)

print(D.mro())
