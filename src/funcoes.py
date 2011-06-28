#!/usr/bin/env python
#*-* coding: utf-8 *-*

#fatorial com recursão
#def fatorial(num):
#    if num <= 1:
#        return 1
#    else:
#        return (num * fatorial(num - 1))
#        
#
#print fatorial(5)


#fibonacci

def fib(n):
    if n > 1:
       return fib(n-1) + fib(n-2)
    else:
        return 1
    
    
for i in [1, 2, 3, 4, 5,6,7,8,9,10]:
    print i, '=>', fib(i)
