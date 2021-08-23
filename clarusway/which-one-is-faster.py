# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:32:21 2021

@author: admin
"""
#which one is faster
from timeit import timeit

def for_loop():
    ls = []
    for i in range(100):
        ls.append(i)
    return ls

 
def list_comp():
    return [i for i in range(100)]
a = timeit(for_loop,number = 100)
b = timeit(list_comp,number = 100)
print( f"List comprehension is {round(a/b)} times faster than foor loop.") #duration of execution


start = timeit.timeit()
ls = [i for i in range(8920000)]
end = timeit.timeit()
print(end - start) 