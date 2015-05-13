#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Léxico

'''
tokens = []
lista_de_caracteres=[]

#Conjunto dos simbolos não reservados em Q0 ex: if "i" é reservado, por isso não está aqui
naoreservado= ["z","b","_","c", "d","f","g","h","j","k","l","m","n","o","a","p","q","r","s","t","u","x","w","y","z"]

alfabeto = ["z","a","_","A","b","B","a","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","v","V","X","Y","y","x","W","w","Z","z"]
numeros = ["z","0","1","2","3","4","5","6","7","8","9"]
palavra=""
letra=""
aux=[]
#Conjunto de todos simbolos validos
valido =["z","_"," ","","0","F","V","1","2","3","4","5","6","7","8","9","a","^","'","a","A","b","B","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","v","X","Y","y","x","W","w","Z","z",",","'","-",";",":","(",")","{","}",""," ","-","\t","\r","\b","R","P","T"," F ","<",">","=","w"]
linhas =1
colunas =1
erroLexico = True
flag = True


# Função incrementalinha, sempre que chamanda, incrementa a linha ou coluna e retorna esses valores 

def incLinha_Coluna(x):
          global linhas
          global colunas
          if x == 0:
                    colunas+=1
                    #print "coluna ",colunas
                    return colunas
          elif x == 1:
                    linhas+=1
                    colunas=0
                    return linhas
#-------------------------------------------------------               
# Função is_numero e is_letra, busca a letra passada pelo parametro e retorna se está contida ou não nas listas alfabeto e numero

def is_numero(letra):
     try:
          if numeros.index(letra):
               return True
        
     except ValueError:
               return False

def is_letra(letra):
     try:
          if alfabeto.index(letra):
               return True
        
     except ValueError:
               return False

               
def is_valido(letra):
     try:
          if valido.index(letra): 
               return True

     except ValueError:
               return False

                
def is_naoReservado(letra):
     try:
          if naoreservado.index(letra):
               return True
      
     except ValueError:
               return False
#------------------------------------------------------- 

def geraLista():
     global lista_de_caracteres
     arquivo = open("teste.txt")
     while True:

          conteudo_texto = arquivo.read(1)
          lista_de_caracteres.append(conteudo_texto)
                         
          if conteudo_texto == '':
               lista_de_caracteres.append("EOF")
               lista_de_caracteres.reverse()
               print lista_de_caracteres
               break      
                       
def showErro(letra):
     global fileb, linhas, erroLexico   	
     erroLexico = False
     
     fileb = open("log.txt", "w")
     fileb.write( "============================================\n")
     fileb.write("ERRO LÉXICO: Caracter ["+letra+"] inválido! \n")
     fileb.write("Linha: "+str(linhas)+"\n")
     fileb.write("Coluna: "+str(colunas)+"\n")
     fileb.write( "============================================\n")
     fileb.close()
   
     print "============================================"
     print "ERRO LÉXICO: Caracter ["+letra+"] Inválido! "
     print "Linha:",linhas
     print "Coluna:",colunas
     print "============================================"
     
#-------------------------------------------------------               

def proximaletra():
     letra = lista_de_caracteres.pop()
     if letra =="\n":
          linha=incLinha_Coluna(1)
          letra = lista_de_caracteres.pop()
     incLinha_Coluna(0)
     return letra
     
#------------= Q0 =-------------------------------------------   

def q0(letra):
     if is_valido(letra):
          while letra =="" or letra ==" ":
               letra=proximaletra()
               
          if (is_letra(letra) or is_numero(letra)):
               q69(letra)
          elif letra == ";":
               q42(letra)
          elif letra== ")":
               q24(letra)
          elif letra == "(":
               q23(letra)
          elif letra == "{":
               q30(letra)
          elif letra== "}":
               q34(letra)
          elif letra== "^":
               q21(letra)
          elif letra == "'":
               q38(letra)
          elif letra== "<":
               q35(letra)
          elif letra == "-":
               q39(letra)
          elif letra== "=":
               q31(letra)
          elif letra== ",":
               q22(letra)
          elif letra== "EOF":
               q22(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)
          

def q21(letra):
     #print "q21:"+letra
     tokens.append("AND")
     exit
     
def q22(letra):
     tokens.append("VIR")
     exit
     
def q23(letra):
     #print "q23:"+letra
     tokens.append("PAE")
     exit
     
def q24(letra):
     tokens.append("PAD")
     exit

def q30(letra):
     #print "q30:"+letra
     tokens.append("CHE")
     exit 
     
def q31(letra):
     letra = proximaletra()
     #print "q31:"+letra
     if is_valido(letra):
          if letra == ":":
               q32(letra)
          else:
               showErro(letra)
     else:
          showErro(letra) 
          
def q32(letra):
     global flag
     letra = proximaletra()
     #print "q32:"+letra
     if is_valido(letra):
          if letra == "=":
               q33(letra)
          else:
               showErro(letra)
     else:
          showErro(letra) 
          
def q33(letra):
     letra = proximaletra()
     #print "q33:"+letra
     if is_valido(letra):
          tokens.append("EQU")
          exit  
     else:
          showErro(letra)   
          
def q34(letra):
     #print "q34:"+letra
     tokens.append("CHD")
     flag=True
     exit  
          
def q35(letra):
     letra = proximaletra()
     #print "q35:"+letra
     if is_valido(letra):
          if letra == "-":
               q36(letra)
          else:
               showErro(letra)
     else:
          showErro(letra) 
          
def q36(letra):
     letra = proximaletra()
     #print "q36:"+letra
     if is_valido(letra):
          if letra == ">":
               q37(letra)
          else:
               showErro(letra)
     else:
          showErro(letra) 
          
def q37(letra):
     letra = proximaletra()
     #print "q37:"+letra
     if is_valido(letra):
          tokens.append("<->")
          exit  
     else:
          showErro(letra)   

def q38(letra):
     #print "q38:"+letra
     tokens.append("NOT")
     exit
     
def q39(letra):
     letra = proximaletra()
     #print "q39:"+letra
     if is_valido(letra):
          if letra == ">":
               q40(letra)
          else:
               showErro(letra)
     else:
          showErro(letra) 
       
def q40(letra):
     letra = proximaletra()
     #print "q40:"+letra
     if is_valido(letra):
          tokens.append("->")
          exit  
     else:
          showErro(letra) 
          
       
def q42(letra):
     tokens.append("PTV") 
     flag=True
     exit  
     
    
def q69(letra):
     global palavra, flag, aux
     palavra += letra
     letra = proximaletra()
     if is_valido(letra):
          if is_letra(letra) or is_numero(letra):
               palavra += letra
               while True:
                    letra = proximaletra()
                    if letra != " ":
                         palavra += letra

                    if (not is_letra(letra) and not is_numero(letra)):
                         
                         teste=palavra
                         teste2=letra
                         q70(teste,teste2)
                         break
                        
          else:     	
               
               teste=palavra
               if teste=='V':
                    tokens.append("TRU")
               elif teste=='v':
                    tokens.append("OR")
               elif teste=='1':
                    tokens.append("TRU")
               elif teste=='0':
                    tokens.append("FAL")
               else:
                
                    tokens.append("VAR")
               palavra=""
               flag=False
               aux.append(letra)
               exit
                         
          
     else:
          showErro(letra)
          
def q70(teste,teste2):
     global palavra, letra, aux, flag
   
     if "Read" == palavra:
          tokens.append("RE")
          palavra=""
          exit
     elif "Print" == palavra:          
          tokens.append("PR")
          palavra=""
          exit
     elif "true" == palavra:
          tokens.append("PR")
          palavra=""
          exit
     elif "false" == palavra:
          tokens.append("FAL")
          palavra=""
          exit
     elif "if" == palavra:
          tokens.append("IF")
          palavra=""
          exit
     elif "else" == palavra:
          tokens.append("ELSE")
          palavra=""
          exit
       
     else:
          tokens.append("VAR")
          palavra=""
          aux.append(teste2)
          flag = False
          exit
                        
def le_token():
     global flag, palavra, letra
     
     if flag == False:
          letra = aux.pop()
          flag=True
     else:
          letra=proximaletra()
          
     q0(letra)
     return tokens.pop()
     
def getErrolexico():
     return erroLexico

def getColunaLinha(x):
     global linhas, colunas
     if x == 0:
          return colunas
     else:
          return linhas
   
 
 
geraLista()  

print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token()
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token() 
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token()
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token()
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token() 
print le_token() 
print le_token()   
print le_token() 
print le_token() 
print le_token()  
print le_token() 
print le_token() 
print le_token()                               


