#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 15:09
# @Author  : wuye
# @File    : type_tip_demo.py
# @Software: PyCharm
from __future__ import annotations

def add(a: int, b: int) -> int:
    return a + b

class MyClass:
    def copy(self) -> MyClass:  # 即使 MyClass 尚未完全定义，也不会报错
        return MyClass()



if __name__ == '__main__':
    print(add(1,2))
    myclass = MyClass()
    myclass.copy()
    print(myclass.copy.__annotations__)
