#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *
import sys 

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
	elif READ(token):
		return True
	elif VAR(token):
		return True
	elif IF(token):
		return True
	else:
		return True #vazio
		
		
					
def PRINT(token):
	print "token no PRINT ",token['nome']
	if token['nome']=="PRI":
		print "oii"
		token = le_token()
		if E1(token):
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
		
		
def VAR(token):
	print "token no VAR ",token['nome']
	if token['nome']=="VAR":
		token = le_token()
		if token['nome']=="ATR":
			token = le_token()
			if E1(token): 
				token = le_token() #nao ta entrando aqui
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
						if IF_linha(token):
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
		
		
def IF_linha(token):
	print "token no IF_linha ",token['nome']
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

		
			
def E0(token):
	print "token no E0 ",token['nome']
	if token['nome']=="VAR":
		token = le_token()
		if E0_linha(token):
			return True
		else: 
			return False		
	else:
		return False
		
def E0_linha(token):
	print "token no E0_linha ",token['nome']
	if E0_asterisco(token):
		return True
	else:
		return False #VAZIOOOOOO

		
def E0_asterisco(token):
	print "token no E0_asterisco ",token['nome']
	if token['nome']=="VIR":
		token = le_token()
		if token['nome']=="VAR":
			token = le_token()
			if E0_linha(token):
				return True
			else:
				return False
						
		else:
			return False
				
	else:
		return False #VAZIOOOOOO
			
		
def E1(token):
	print "token no E1 ",token['nome']
	if E2(token):
		token = le_token()
		if E1_linha(token):
			return True
		else:
			return False
			
	else:
		return False
		

def E1_linha(token):
	print "token no E1_linha ",token['nome']
	if E1_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
		
def E1_asterisco(token):
	print "token no E1_asterisco ",token['nome']
	if token['nome']=="EQU":
		token = le_token()
		if E2(token):
			token = le_token()
			if E1_linha(token):
				return True
			else:
				return False
					
		else:
			return False
			
	else:
		return False
		
		
def E2(token):
	print "token no E2 ",token['nome']
	if E3(token):
		token = le_token()
		if E2_linha(token):
			return True
		else:
			return False
			
	else:
		return False
		
		
def E2_linha(token):
	print "token no E2_linha ",token['nome']
	if E2_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
		
def E2_asterisco(token):
	print "token no E2_asterisco",token['nome']
	if token['nome']=="IMP":
		token = le_token()
		if E3(token):
			token = le_token()
			if E2_linha(token):
				return True
			else:
				return False
				
		else:
			return False
			
	else:
		return False
		
		
def E3(token):
	print "token no E3",token['nome']
	if E4(token):
		token = le_token()
		if E3_linha(token):
			return True
		else:
			return False
			
	else:
		return False
		
		
def E3_linha(token):
	print "token no E3_linha",token['nome']
	if E3_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
		
def E3_asterisco(token):
	print "token no E3_asterisco",token['nome']
	if token['nome']=="AND":
		token = le_token()
		if E4(token):
			token = le_token()
			if E3_linha(token):
				return True
			else:
				return False
				
		else:
			return False
			

	elif token['nome']=="OR":
		token = le_token()
		if E4(token):
			token = le_token()
			if E3_linha(token):
				return True
			else:
				return False
				
		else:
			return False
			
	else:
		return False
		
		
def E4(token):
	print "token no E4",token['nome']
	if FINAL(token):
		token = le_token()
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
	if E4_asterisco(token):
		return True
	else:

		return False #VAZIOOOO
		
		
def E4_asterisco(token):
	print "token no E4_asterisco",token['nome']
	if token['nome']=="NOT":
		token = le_token()
		if E4_linha(token):
			return True
			
		else:
			return False
			
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
		
		
			
		
#parametro = sys.argv[1:]

entrada = "TestFile/test3.txt"
geraLista(entrada) 


token = le_token()
print S_linha(token)
	

		



	
