#!/usr/bin/env python

numero = raw_input("Insert a number: ")
myList = [39,48,22,1,4]

if  int(numero) in myList:
    print "The number " + numero + " is in the list."
else:
    print "Sorry, but this number is not contained in the list."
