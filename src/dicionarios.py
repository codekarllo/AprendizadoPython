#!/usr/bin/env python
#*-* coding: utf-8 *-*

dic = {'Daddy Yankee':['DY Munidal','DY Prestige'], 'Pitbull': ['MIAMI','Planet Pit']}

items  = dic.items()
keys   = dic.keys()
values = dic.values()

for artista,albuns in dic.items():
    print artista, '=>', albuns

#se existir o artista pitbull, deleta
if dic.has_key('Pitbull'):
    del dic['Pitbull']

#matriz esparsa com dicionarios
#dim = 6,12
#mat = {}
#
#mat[3, 7] = 3
#mat[4, 6] = 5
#mat[6, 3] = 7
#mat[5, 4] = 6
#mat[2, 9] = 4
#mat[1, 0] = 9
#
#for lin in range(dim[0]):
#    for col in range(dim[1]):
#        print mat.get((lin,col),0),
#    print


# Matriz em forma de string
matriz = '''000000000000
900000000000
000000000400
000000030000
000000500000
000060000000'''

mat = {}

for lin, linha in enumerate(matriz.splitlines()):
    for col,coluna in  enumerate(linha.split()):
        coluna = int(coluna)
        if coluna:
            mat[lin,col] = coluna
            
print mat
