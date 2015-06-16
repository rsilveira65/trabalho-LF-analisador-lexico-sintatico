#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *
def s_linha(token):
	print token['nome']
	if token['nome'] =="PR":
		s(token)
	elif token== "VAR":
		s(token)
	elif token['nome']== "REA":
		#print "auheiahe"
		Read(token)
	elif token['nome']== "IF":
		s(token)
	elif token['nome']== "VAR":
		s(token)
	elif token['nome']== "EOF":
		print "Aceito pelo Analisador Sintatico"
		
def s(token):
	print token['nome']
	if token['nome'] =="PR":
		Print(token)
	elif token['nome']== "REA":
		Read(token)
	elif token['nome']== "VAR":
		Var(token)
	elif token['nome']== "IF":
		If(token)
	
		
def Read(token):
	token = le_token()
	print token['nome']
	if token['nome'] =="VAR":
		Var(token)

def Print(token):
	token = le_token()
	print token['nome']
	if token['nome'] =="VAR":
		Var(token)
		
def Var(token):
	token = le_token()
	print token['nome']
	if token['nome'] =="PTV":
		token = le_token()
		print token['nome']
		s_linha(token)

	
		
token = le_token()		
s_linha(token)

		



	
