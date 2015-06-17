#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *

def s(token):
	print token
	if token['nome']=='VIR':

		return 1
	else:
		if token['nome']=='IMP':
			
			token = le_token()
			print token
			if B(token):
				return 1
			else:
				return 0
		else:
			return 0
			
def B(token):
	print token
	if token['nome']=="^":
		B(token)
	elif token['nome']=="EOF":
		#print token
		return 1
	else:
		return 0
		
		
	
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

		



	
