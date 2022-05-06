# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:38:17 2022

@author: lawon
"""
# x=5.0, y=3을 입력하고, 결과창으로
# "x+y=8.0 입니다"를 출력하는 함수 작성
x = 5.0
y = 3

def plus():
    print(f"\"x + y = {x+y}입니다.\"")

plus()

# x="than3k"
# y="yo97u"
# x와 y를 위와 같이 선언한 후에, thank you를 출력하라.
x="than3k"
y="yo97u"

x = x.replace("3", "")
y = y.replace("97", "")

plus()

val = [100,200,300]
for i, v in enumerate(val):
    print(i, v)
    
    
lst = list(range(9))
lst_odd = [x for x in lst if x%2==1]
lst_even = [x for x in lst if x%2==0]
print(lst_odd)
print(lst_even)


def sum(num, *ar):
    print(num, ar)

def mean(**kwargs):
    print(kwargs)
#sum(1,2,3,4)
mean(asdf=1, abd234=4)


class calculator() :
    def __init__(self, x):
        self.x = x
    
    def add(self, value) :
        self.x += value
        
    def sub(self, value) :
        self.x -= value
        
cal = calculator(3)
cal.add(100)
print(cal.x)
cal.sub(1000)
print(cal.x)