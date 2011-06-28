#!/usr/bin/env python
#*-* coding: utf-8 *-*

#brit progs
progs = ['YES','Genesis','Pink Floyd','ELP']

#varrendo a lista
for prog in progs:
    print prog
    

#trocando ultimo elemento
progs[-1] = 'King Crismon'

#incluindo
progs.append('Reggaeton')

#removendo
progs.remove('Reggaeton')

#ordenando
progs.sort()

#inverte a lista
progs.reverse()

#imprime numerado

for  num, value in enumerate(progs):
    print  num, value

#imprime segundo item em diante
print progs[1:]