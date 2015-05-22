from analisador_lexico import *
def exp(token):
	token = le_token()
	print token['nome']
	if token['nome'] =="CHE":
		token = le_token()
		if token== "VAR":
			token = le_token()
			print token
			if token['nome'] =="CHD":
				token = le_token()
				if token['nome'] =="PTV":
					print "Atribuicao"
				else:
					print "nao deu"
			else: 
				print "ops"
		else:
			print "nao foi por ai"	
	
			
	elif token['nome'] =="VAR":
		token = le_token()
		print token
		if token['nome'] =="PTV":
			print "Atribuicao2"
		else:
			print "nonono"
	
def s(token):
	if token['nome'] == "VAR":
		token = le_token()
		print token
		if token['nome'] =="ATR":
			exp(token)
		else:
			print "deu merda1"
	else:
		print token['nome']
		print "deu merda2"
	
if getErrolexico() == True:
	token = le_token()
	s(token)
	
