#!/usr/bin/env python
#*-* coding: utf-8 *-*
import string
import UserString
#print 'Python'[::-1]

#st = string.Template('$aviso aconteceu em $quando')
#s = st.substitute({'aviso':'Falta de eletricidade','quando':'17 de junho de 2011'})
#print s

#def alerta(tipoAlerta):
#    msgAlerta = ""
#    alertaTemplate = string.Template('$tipo: $mensagem')
#    
#    if tipoAlerta == "1":
#        msgAlerta = alertaTemplate.substitute({'tipo': 'Perigo', 'mensagem': 'Há uma pane na aeronave!'})
#    elif tipoAlerta == "2":
#        msgAlerta = alertaTemplate.substitute({'tipo': 'Advertência', 'mensagem': 'Foi detectado algo de errado na aeronave.'})
#    elif tipoAlerta == "3":
#        msgAlerta = alertaTemplate.substitute({'tipo': 'Desastre', 'mensagem': "Mayday! Mayday!"})    
#    else:
#        msgAlerta = "Opção inválida."
#    return msgAlerta
#
#tipoMsg = raw_input("Qual tipo de aviso que você deseja enviar? \nOpções: \n1-Perigo \n2-Advertência \n3-Desastre \n")
#print alerta(tipoMsg)

#----------------------------------------------------
# Strings Mutáveis
#s = UserString.MutableString('Python')
#s[0] = 'p'
#print s

#-------------------------------------------------------
# Strings unicode
u = u'Hüsker Dü'
s = u.encode('latin1')
print s,'=>', type(s)


s = 'Hüsker Dü'
u = s.decode('latin1')
print repr(u), '=>', type(u)