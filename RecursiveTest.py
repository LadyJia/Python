#!/usr/bin/env python3
#汉诺塔的移动
#递归初接触

def my_recursive(n,a,b,c):
    if n == 1:
        print('移动',a,'-->',c)
    else:
        my_recursive(n-1,a,c,b)
        my_recursive(1,a,b,c)
        my_recursive(n-1,b,a,c)

my_recursive(10,'A','B','C')