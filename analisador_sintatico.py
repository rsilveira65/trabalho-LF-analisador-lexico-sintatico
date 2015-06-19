#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *
import sys 

pilha=[]

def s_linha(token):
		pilha.append({'nome':'slinha', 'tipo':'variavel')
		pilha.append({'nome':'fim', 'tipo':'fim')
		S(token)
			
def S(token):
	if token['nome']=="PRI" or token['nome']=="VAR" or  token['nome']=="IF" or  token['nome']=="REA":
		print token
		
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
		
		
#parametro = sys.argv[1:]

entrada = "TestFile/test3.txt"
geraLista(entrada) 

while getErrolexico() or token['nome']!="+":
	token = le_token()
	print token
	s_linha(token)
	

		



	
