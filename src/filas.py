#!/usr/bin/env python
#*-* coding: utf-8 *-*

lista = ['A','B','C']
print lista

#retira todos elementos de uma lista, emulando uma fila
while lista:
    print 'Saiu ', lista.pop(0), ' restam',len(lista)
    
lista+= ['D','E','F']
print lista

#pilha quem sai primeiro é o ultimo que entrou
while lista:
    print 'saiu ',lista.pop(), ' restam', len(lista)
    



