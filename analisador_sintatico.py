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
		if S(token):
			token = le_token()
			if token['nome']=="+":
				return True
			else:
				return False
				
		else:
			return False
			
		
			
def S(token):   #ADICIONAR O VAZIO
	print "token no s ",token['nome']
	if PRINT(token):
		return True
	else:
		if READ(token):
			return True
		else:
			if VAR(token):
				return True
			else:
				if IF(token):
					return True
				else:
					return False #vazio
		
		
					
def PRINT(token):
	print "token no PRINT ",token['nome']
	if token['nome']=="PRI":
		token = le_token()
		if E0(token):
			token = le_token()
			if token['nome'] =="PTV":
				token = le_token()
				if S(token):
					return True
				else:
					return False

			else:
				return False
		else:
			return False
			
	else:
		return False
		
def READ(token):
	print "token no READ",token['nome']
	if token['nome']=="REA":
		token = le_token()
		if EVIR(token):
			token = le_token()
			if token['nome'] =="PTV":
				token = le_token()
				if S(token):
					return True
				else:
					return False	
			else:
				return False
		else:
			return False	
	else:
		return False
		
def VAR(token):
	print "token no VAR",token['nome']
	if token['nome']=="VAR":
		token = le_token()
		if token['nome']=="ATR":
			token = le_token()
			if E1(token):
				token = le_token()
				if token['nome']=="PTV":
					token = le_token()
					if S(token):
						return True
					else:
						return False	
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False
		
		
		
def E0(token):
	print "token no E0 ",token['nome']
	if E1(token):
		token = le_token()
		empilha({'nome':'E0_linha','tipo':'variavel'})
		if E0_linha(token):
			return True
		else:
			return False
	else:
		return False
		
		
def E0_linha(token):
	print "token no E0_linha ",token['nome']
	if token['nome']=="VIR":
		token = le_token()
		empilha({'nome':'E0_linha','tipo':'variavel'})
		if E1(token):
			token = le_token()
			if E0_linha(token):
				return True
			else:
				return False
		else:
			return False
	else:
		return False #VAZIO!
		
def EVIR(token):
	print "token no EVIR ",token['nome']
	if token['nome']=="VAR":
		token = le_token()
		if EVIR_linha(token):
			return True
		else:
			return False
	else:
		return False
		
def EVIR_linha(token):
	print "token no EVIR_linha ",token['nome']
	if token['nome']=="VIR":
		token= le_token()
		if token['nome']=="VAR":
			token= le_token()
			if EVIR_linha(token):
				return True
			else:
				return False
		else:
			return False
	else:
		return False #VAZIO

def E1(token):
	print "token no E1 ",token['nome']
	if E2(token):
		token = le_token()
		empilha({'nome':'E1_linha','tipo':'variavel'})
		if E1_linha(token):
			return True
		else:
			return False			
	else:
		return False
		

def E1_linha(token):
	print "token no E1_linha ",token['nome']
	if token['nome']=="EQU":
		token = le_token()
		empilha({'nome':'E1_linha','tipo':'variavel'})
		if E2(token):
			token = le_token()
			if E1_linha(token):
				token = le_token
			else: 
				return False
		else:
			return False
	else:
		return False #VAZIO
	
def E2(token):
	print "token no E2 ",token['nome']
	if E3(token):
		token = le_token()
		empilha({'nome':'E2_linha','tipo':'variavel'})
		if E2_linha(token):
			return True
		else:
			return False
	else:
		return False
		
def E2_linha(token):
	print "token no E2_linha ",token['nome']
	if token['nome']=="IMP":
		token = le_token()
		empilha({'nome':'E2_linha','tipo':'variavel'})
		if E3(token):
			token = le_token()
			if E2_linha():
				return True
			else:
				return False
		else:
			return False
	else:
		return False #vazio
		
def E3(token):
	print "token no E3",token['nome']
	if E4(token):
		token = le_token()
		empilha({'nome':'E3_linha','tipo':'variavel'})
		if E3_linha(token):
			return True
		else:
			return False		
	else:
		return False
		
		
def E3_linha(token):
	print "token no E3_linha",token['nome']
	if token['nome']=="AND":
		token = le_token()
		if E3(token):
			return True
		else: 
			return False
				
	elif token['nome']=="OR":
		token = le_token()
		if E3(token):
			return True
		else: 
			return False 
	else:
		return False #VAZIOOOO

def E4(token):
	print "token no E4",token['nome']
	if FINAL(token):
		token = le_token()
		empilha({'nome':'E4_linha','tipo':'variavel'})
		if E4_linha(token):
			return True
		else:
			return False		
	
	elif token['nome']=="PAE":
		token = le_token()
		if E1(token):
			token = le_token()
			if token['nome']=="PAD":
				token = le_token()
				if E4_linha(token):
					return True
				else:
					return False	
			else:
				return False		
		else:
			return False	
	else:
		return False
		
		
def E4_linha(token):
	print "token no E4_linha",token['nome']
	if token['nome']=="NOT":
		token = le_token()
		if E4_linha(token):
			return True
		else:
			return False
	else:
		return False #VAZIOOO

		
def IF(token):
	print "token no IF ",token['nome']
	if token['nome']=="IF":
		token = le_token()
		if E1(token):
			token = le_token()
			if token['nome']=="CHE":
				token = le_token()
				if S(token):
					token = le_token()
					if token['nome']=="CHD":
						token = le_token()
						if ELSE(token):
							return True
						else:
							return False
						
					else:
						return False
					
				else:
					return False
				
			else:
				return False
			
		else:
			return False

	else:
		return False	


def ELSE(token):
	print "token no ELSE ",token['nome']
	if token['nome']=="ELS":
		token = le_token()
		if token['nome']=="CHE":
			token = le_token()
			if S(token):
				token = le_token()
				if token['nome']=="CHD":
					token = le_token()
					if S(token):
						return True

					else:
						return False

				else:
					return False
					
			else:
				return False
				
		else:
			return False
			
	elif S(token):
			return True
		
	else:
		return False			
		
	

def FINAL(token):
	print "token no FINAL",token['nome']
	if token['nome']=="VAR":
		return True
	elif token['nome']=="FAL":
		return True
	elif token['nome']=="TRU":
		return True
	else:
		return False
		
def precisodormir(token):
	while TOP != "EOF" or token != "+":
		TOP = desempilha()
		if TOP == "EOF" and token == "+":
			return True
		elif "token" == TOP['tipo']:
			
			if "variavel" == TOP['tipo']:
				desempilha()
				token = le_token()
			else:
				print "erro :("
		else:
			print S_linha(token)
			aux = desempilha()
			if aux['tipo']== "variavel":
				if aux["nome"] == "E0_linha":
					token = le_token;
					E0_linha(token)
					
				elif aux["nome"] == "E1_linha":
					token = le_token;
					E1_linha(token)
					
				elif aux["nome"] == "E2_linha":
					token = le_token;
					E2_linha(token)
					
				elif aux["nome"] == "E3_linha":
					token = le_token;
					E3_linha(token)
				else:
					print "..."
			else:
				print "..."	
		
#parametro = sys.argv[1:]

entrada = "TestFile/test3.txt"
geraLista(entrada) 


token = le_token()
empilha({'nome':'EOF','tipo':'token'})
empilha({'nome':'S_linha','tipo':'variavel'})
precisodormir(token)


				
			
				
			
	 	

		

		



	
