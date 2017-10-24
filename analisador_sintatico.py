#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *
import sys 

pilha=[]

def empilha(token):
	global pilha
	pilha.append(token)
	
def desempilha():
	global pilha
	return pilha.pop()
	

def ShowErroSintatico(regra):
	
	global fileb, linhas, erroLexico
	print "ERRO SINTATICO na regra: ",regra
	#print "linha:",linhas
	#print "coluna:",colunas
  

def S_linha(token):
		print "token no s_linha ",token['nome']
		TOP = pilha.pop()
		empilha({'nome':'S','tipo':'variavel'})
		if S(token):
			return True
		else:
			return False
		
			
def S(token):   
	print "token no S ",token['nome']
	TOP = pilha.pop()
	token = le_token()
	if (token['nome'] == "PRI"):
		# token = le_token()
		PRINT(token)
		return True
	if token['nome'] == "REA":
		# token = le_token()
		READ(token)
		return True
	if token['nome'] == "VAR":
		# token = le_token()
		VAR(token)
		return True	
	if token['nome'] == "IF":
		# token = le_token()
		IF(token)
		return True
	if (token['nome'] != "PRI") and (token['nome'] != "REA") and  (token['nome'] != "VAR") and (token['nome'] != "IF"):
		return False
		
					
def PRINT(token):
	print "token no PRINT ",token['nome']
	empilha({'nome':'S','tipo':'variavel'})
	empilha({'nome':'PTV','tipo':'token'})
	empilha({'nome':'E0','tipo':'variavel'})
	return True
	
	
		
def READ(token):
	print "token no READ",token['nome']
	empilha({'nome':'S','tipo':'variavel'})
	empilha({'nome':'PTV','tipo':'token'})
	empilha({'nome':'EVIR','tipo':'variavel'})
	return True
		
def VAR(token):
	print "token no VAR",token['nome']
	empilha({'nome':'S','tipo':'variavel'})
	empilha({'nome':'PTV','tipo':'token'})
	empilha({'nome':'E1','tipo':'variavel'})
	empilha({'nome':'ATR','tipo':'token'})
	return True
		
		
def E0(token):
	print "token no E0 ",token['nome']
	empilha({'nome':'E0_linha','tipo':'variavel'})
	if E1(token):
		return True
	else:
		return False
		
		
def E0_linha(token):
	print "token no E0_linha ",token['nome']
	E0_ast(token)
		
def E0_ast(token):
	print "token no E0_ast ",token['nome']
	empilha({'nome':'E0_linha','tipo':'variavel'})
	empilha({'nome':'E1','tipo':'variavel'})
	empilha({'nome':'VAR','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
	if cmp (TOP['nome'], token['nome']) == 0:
		return True			
	else:
		return False

		
def EVIR(token):
	print "token no EVIR ",token['nome']
	empilha({'nome':'EVIR_linha','tipo':'variavel'})
	empilha({'nome':'VAR','tipo':'token'})
	TOP =  pilha.pop()
	token = le_token()
	if cmp (TOP['nome'], token['nome']) == 0:
		return True
	else:
		return False
	 
def EVIR_linha(token):
	print "token no EVIR_linha ",token['nome']
	EVIR_ast(token)
	
def EVIR_ast(token):
	
	print "token no EVIR_ast ",token['nome']
	empilha({'nome':'EVIR_linha','tipo':'variavel'})
	empilha({'nome':'VAR','tipo':'token'})
	empilha({'nome':'VIR','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
		
	if cmp (TOP['nome'], token['nome']) == 0:
		TOP = pilha.pop()
		token = le_token()
		
		if cmp (TOP['nome'], token['nome']) == 0:
			return True
		else: 
			return False
	else:
		return False
					
def E1(token):
	print "token no E1 ",token['nome']
	empilha({'nome':'E1_linha','tipo':'variavel'})
	empilha({'nome':'E2','tipo':'variavel'})	
	# E2(token)	
	return True	
		
def E1_linha(token):
	print "token no E1_linha ",token['nome']
	E1_ast(token)
	
def E1_ast(token):
	print "token no E1_ast ",token['nome']
	
	empilha({'nome':'E1_linha','tipo':'variavel'})
	empilha({'nome':'E2','tipo':'variavel'})
	empilha({'nome':'EQU','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
	if cmp (TOP['nome'], token['nome']) == 0:
		return True
	else: 
		return False
	
def E2(token):
	print "token no E2 ",token['nome']
	empilha({'nome':'E2_linha','tipo':'variavel'})
	empilha({'nome':'E3','tipo':'variavel'})
	# E3(token)
	
		
def E2_linha(token):
	print "token no E2_linha ",token['nome']
	E2_ast(token)
	
def E2_ast(token):
	print "token no E2_ast ",token['nome']
	empilha({'nome':'E2_linha','tipo':'variavel'})
	empilha({'nome':'E3','tipo':'variavel'})
	empilha({'nome':'IMP','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
	if cmp (TOP['nome'], token['nome']) == 0:
		return True
	else: 
		return False
		
def E3(token):
	print "token no E3",token['nome']
	empilha({'nome':'E3_linha','tipo':'variavel'})
	empilha({'nome':'E4','tipo':'variavel'})
	# E4(token)	
		
def E3_linha(token):
	global pilha
	print "token no E3_linha",token['nome']
	empilha({'nome':'E3','tipo':'variavel'})
	token = le_token()
	print "oii"
	print token
	if token['nome']=="AND": 	
		print "oii2"	
		empilha({'nome':'E3','tipo':'variavel'})
		
		return True
	elif cmp (token['nome'],"OR")==0:
		empilha({'nome':'E3','tipo':'variavel'})
		return True
	else:
		return False 
			
def E4(token): #REVISAR
	print "token no E4",token['nome']
	empilha({'nome':'E3_linha','tipo':'variavel'})
	if (token['nome'] == "PAE"):
		empilha({'nome':'E4_linha','tipo':'variavel'})
		empilha({'nome':'PAD','tipo':'token'})
		empilha({'nome':'E1','tipo':'variavel'})
		empilha({'nome':'PAE','tipo':'token'})
		TOP = pilha.pop()
		if cmp (TOP['nome'], token['nome']) == 0:
			return True
		else:
			return False
	else:
		empilha({'nome':'E4_linha','tipo':'variavel'})
		empilha({'nome':'FINAL','tipo':'variavel'})
		return True

		
def E4_linha(token):
	print "token no E4_linha ",token['nome']
	E4_ast(token)
			
def E4_ast(token):
	print "token no E4_ast",token['nome']
	empilha({'nome':'E4_linha','tipo':'variavel'})
	empilha({'nome':'NOT','tipo':'token'})
	TOP = pilha.pop()
	token = le_token()
	#print token
	if cmp (TOP['nome'], token['nome']) == 0:
		return True
	else: 
		return False
		
def IF(token): 
	print "token no IF",token['nome']
	if token['nome'] == "IF":
		empilha({'nome':'ELSE','tipo':'variavel'})
		empilha({'nome':'CHD','tipo':'token'})
		empilha({'nome':'S','tipo':'variavel'})
		empilha({'nome':'CHE','tipo':'token'})
		empilha({'nome':'E1','tipo':'variavel'})
		empilha({'nome':'IF','tipo':'token'})
	if cmp (TOP['nome'], token['nome']) == 0:
		E1(token)
		# return True
	else:
		return False
	
def ELSE(token):
	print "token no ELSE",token['nome']
	if token['nome'] == "ELS":	
		empilha({'nome':'S','tipo':'variavel'})
		empilha({'nome':'CHD','tipo':'token'})
		empilha({'nome':'S','tipo':'variavel'})
		empilha({'nome':'CHE','tipo':'token'})
		empilha({'nome':'ELS','tipo':'token'})
		return True
	else:
		empilha({'nome':'S','tipo':'variavel'})
		return True
		
def FINAL(token):
	global TOP, pilha
	print "token no FINAL",token['nome']
	if token['nome']=="VAR":
		return True
	elif token['nome']=="FAL":
		return True
	elif token['nome']=="TRU":
		return True
	else:
		return False
	#TOP = pilha.pop()
	#print pilha 
	#print TOP
	#token = le_token()
	#if cmp (TOP['nome'], token['nome']) == 0:
		#return True
	#else:
		#return False
			
	
def sintatico(token):
	TOP = "entrada"
	while TOP != "EOF" or token != "+":
		print "aqui ",token
		if pilha: #testa se a pilha n ta vazia
			TOP = pilha.pop()
			print pilha
			if TOP == "EOF" and token == "+": #teste se o topo da pilha é EOF e token "+"
				return True
			elif "token" == TOP['tipo']:
				
				if "variavel" == TOP['tipo']:
					#TOP = pilha.pop()
					token = le_token()
				else:
					print "erro :("
			
			else:
				if pilha:
					empilha(TOP)
					print pilha
					TOP = pilha.pop()
					print pilha
					if cmp (TOP['nome'], "S_linha") == 0:
						S_linha(token)
					elif cmp (TOP['nome'], "S") == 0:
						S(token) 	
					
					elif cmp (TOP['nome'], "E0") == 0:
						E0(token) 	
						
					elif cmp (TOP['nome'], "E0_linha") == 0:
						(token) 	
						
					elif cmp (TOP['nome'], "E0_ast") == 0:
						E0_ast(token) 	
						
					elif cmp (TOP['nome'], "E1") == 0:
						E1(token) 	
						
					elif cmp (TOP['nome'], "E1_linha") == 0:
						E1_linha(token) 	
						
					elif cmp (TOP['nome'], "E1_ast") == 0:
						E1_ast(token) 	
						
					elif cmp (TOP['nome'], "E2") == 0:
						E2(token) 	
						
					elif cmp (TOP['nome'], "E2_linha") == 0:
						E2_linha(token) 	
						
					elif cmp (TOP['nome'], "E2_ast") == 0:
						E2_ast(token) 	
						
					elif cmp (TOP['nome'], "E3") == 0:
						E3(token) 	
						
					elif cmp (TOP['nome'], "E3_linha") == 0:
						E3_linha(token) 	
						
					elif cmp (TOP['nome'], "E4") == 0:
						E4(token) 	
						
					elif cmp (TOP['nome'], "E4_linha") == 0:
						E4_linha(token) 	
						
					elif cmp (TOP['nome'], "E4_ast") == 0:
						E4_ast(token) 	
						
					elif cmp (TOP['nome'], "IF") == 0:
						IF(token) 	
						
					elif cmp (TOP['nome'], "FINAL") == 0:
						FINAL(token) 	
		else:
			return False
	return True
#parametro = sys.argv[1:]

entrada = "TestFile/test3.txt"
geraLista(entrada) 


token = le_token()
empilha({'nome':'EOF','tipo':'token'})
empilha({'nome':'S_linha','tipo':'variavel'})
print pilha
print sintatico(token)