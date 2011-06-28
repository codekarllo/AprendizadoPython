#!/usr/bin/env python
#*-* coding: utf-8 *-*

#set

s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))
print 's1:',s1, '\ns2:',s2,'\ns3:',s3

#range(inicio,fim,intervalo)
#s =  range(0,14,2)
#print s

#união de conjuntos
s1s2 = s1.union(s2)
print 'União s1 com s2',s1s2

#diferença de conjuntos
print 'Diferença s1s2 com s3' ,s1s2.difference(s3)

#intersecção de conjuntos
print 'Intersecção s1s2 com s3 ', s1s2.intersection(s3)

#testa se um set inclui o outro
if s1.issuperset([1,2]):
    print 's1 inclui 1 e 2'
    
#testa se não existe elementos em comum
if s1.isdisjoint(s2):
    print 's1 e s2 n tem elementos em comum'