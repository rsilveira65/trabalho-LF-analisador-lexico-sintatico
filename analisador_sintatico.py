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
	
	if token['nome']=="PRI":
		pilha.append({'nome':'s', 'tipo':'variavel')
		pilha.append({'nome':token['nome'], 'tipo':'token')
		PRI(token)  
		#print token
		
	elif token['nome']== "IF":
		pilha.append({'nome':'s', 'tipo':'variavel')
		pilha.append({'nome':token['nome'], 'tipo':'token')
		IF(token)  
	
	elif token['nome']== "REA":
		pilha.append({'nome':'s', 'tipo':'variavel')
		pilha.append({'nome':token['nome'], 'tipo':'token')
		REA(token)  

	elif token['nome']=="VAR":
		pilha.append({'nome':'s', 'tipo':'variavel')
		pilha.append({'nome':token['nome'], 'tipo':'token')
		VAR(token)  
				
	else:
		"errrrrou"
					
def PRI(token):
	test = pilha.remove() 
	while test['tipo'] == "token":
		pilha.append({'nome':'s', 'tipo':'variavel')
		pilha.append({'nome':token['nome'], 'tipo':'token')
		pilha.append({'nome':'s', 'tipo':'variavel')
		test = pilha.remove() 
		
		
		
def IF(token):
	token = le_token()
	print token
	FINAL(token)
	if token['nome']=="PTV":
		S(token)
		
def VAR(token):
	token = le_token()
	print token
	FINAL(token)
	if token['nome']=="PTV":
		S(token)

def REA(token):
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
	

		



	
