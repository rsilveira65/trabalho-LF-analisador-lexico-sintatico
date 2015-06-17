#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *

def s_linha(token):
	print token
	if token['nome']=="+":
		return 1
	else:
		if token['nome']=="PRI":
			print token
			S(token)



def S(token):
	token = le_token()
	print token
	if token['nome']=="PRI":
		PRI(token)
					
def PRI(token):
	token = le_token()
	print token
	FINAL(token)
	if token['nome']=="PTV":
		S(token)
		
def FINAL(token):
	token = le_token()
	print token
	E1(token)
	if token['nome']=="PTV":
		S(token)
		
		
		
	
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token

token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token
token = le_token()
print token









#print s(token)

		



	
