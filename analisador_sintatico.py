#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Sintático
'''
from analisador_lexico import *
import sys 


def s_linha(token):
		if S(token):
			token = le_token()
			if token['nome']="+":
				return True
			else: 
				return False
		else:
			return False
		
			
def S(token):   #ADICIONAR O VAZIO
	if PRINT(token):
		return True
	elif READ(token):
		return True
	elif VAR(token):
		return True
	elif IF(token):
		return True
	else:
		return False
		
					
def PRINT(token):
	if token['nome']="PRI":
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
	if token['nome']="REA":
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
	if token['nome']="VAR":
		token = le_token()
		if token['nome']="ATR":
			token = le_token()
			if E1(token):
				token = le_token()
				if token['nome']="PTV":
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
	if token['nome']="IF":
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
		
def IF_linha(token):
	if token['nome']="ELS":
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
	else:
		if S(token):
			return True
		else:
			return False
			
def E0(token):
	if token['nome']="VAR":
		token = le_token()
		if E0_linha(token):
			token = le_token()
			return True
		else: 
			return False
	else:
		False
		
def E0_linha(token):
	if E0_asterisco(token):
		return True
	else:
		return False #VAZIOOOOOO
		
def E0_asterisco(token):
	if token['nome']="VIR":
		token = le_token()
		if token['nome']="VAR":
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
	if E2(token):
		token = le_token()
		if E1_linha(token):
			return True
		else:
			return False
	else:
		return False

def E1_linha(token):
	if E1_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
def E1_asterisco(token):
	if token['nome']="EQU":
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
	if E3(token):
		token = le_token()
		if E2_linha(token):
			return True
		else:
			return False
	else:
		return False
		
def E2_linha(token):
	if E2_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
def E2_asterisco(token):
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
	if E4(token):
		token = le_token()
		if E3_linha(token):
			return True
		else:
			return False
	else:
		return False
		
def E3_linha(token):
	if E3_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
def E3_asterisco(token):
	if token['nome']=="AND":
		token = le_token()
		if E4(token):
			token = le_token()
			if E3_linha(token):
				return True
			else:
				return False
	elif:
		if token['nome']=="OR":
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
	if FINAL(token):
		token = le_token()
		if E4(token):
			return True
		else:
			return False
	elif:
		if token['nome']=="PAE":
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
	else:
		return False
		
def E4_linha(token):
	if E4_asterisco(token):
		return True
	else:
		return False #VAZIOOOO
		
def E4_asterisco(token):
	if token['nome']=="NOT":
		token = le_token()
		if E4_linha(token):
			return True
		else:
			return False
	else:
		return False

def FINAL(token):
	if token['nome']=="VAR":
		return True
	elif token['nome']=="FAL":
		return True
	if token['nome']=="TRU":
		return True
	else:
		return False
		
			
		
#parametro = sys.argv[1:]

entrada = "TestFile/test3.txt"
geraLista(entrada) 


	token = le_token()
	s_linha(token)
	

		



	
