#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
from Tkinter import *
import tkMessageBox
import Tkinter
import urllib
import base64
from tkFileDialog   import askopenfilename


'''
@author: Rafael Silveira rsilveira@inf.ufpel.edu.br
Analisador Léxico
'''
tokens = []
lista_de_caracteres=[]

alfabeto = ["z","a","_","A","b","B","a","C","c","D","d","0","1","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","v","V","X","Y","y","x","W","w","Z","z"]
numeros = ["z","0","1","2","3","4","5","6","7","8","9"]
palavra=""
letra=""
aux=[]
lista_token=[]
#Conjunto de todos simbolos validos
valido =["z","_"," ","","0","F","V","1","2","3","4","5","6","7","8","9","a","^","'","a","A","b","B","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","v","X","Y","y","x","W","w","Z","z",",","'","-",";",":","(",")","{","}",""," ","-","\t","\r","\b","R","P","T"," F ","<",">","+","=","w"]
linhas =1
colunas =1
erroLexico = True
flagVariavel = False

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

#-------------------------------------------------------
#   abre o arquivo de entrada e carrega todos caracteres para uma lista


#-------------------------------------------------------
def showErro(letra):
     global fileb
     global linhas
     global erroLexico
     erroLexico = True

     fileb = open("log.txt", "w")
     #fileb.write( "============================================\n")
     fileb.write("ERRO LÉXICO: Caracter "+letra+" inválido! \n")
     fileb.write("Linha: "+str(linhas)+"\n")
     fileb.write("Coluna: "+str(colunas)+"\n")
     #fileb.write( "============================================\n")
     fileb.close()

     print "============================================"
     print "ERRO LÉXICO: Caracter "+letra+" inválido! "
     print "Linha:",linhas
     print "Coluna:",colunas
     print "============================================"

#-------------------------------------------------------

def proximaletra():
     global colunas, linhas
     if lista_de_caracteres:
          letra = lista_de_caracteres.pop() #retira letra da lista
          while letra =="\n":    #caso seja uma quebra de linha, incrementa linha
               linha=incLinha_Coluna(1)
               letra = lista_de_caracteres.pop()
          while letra =="\t":    #caso seja um tab, incrementa coluna 3 vezes
               incLinha_Coluna(0)
               incLinha_Coluna(0)
               incLinha_Coluna(0)
               letra = lista_de_caracteres.pop()
          incLinha_Coluna(0)
          return letra
     else:
          print "Acabou os caracteres"
          return

#------------= Q0 =-------------------------------------------

def q0(letra):
     if is_valido(letra):
          while letra =="" or letra ==" ":  #enquanto for espaço, disconsidera e le proxima letra
               letra=proximaletra()
          if is_letra(letra): #caso seja uma letra vai para estado 19
               q19(letra)
          elif letra== "^":
               q1(letra)
          elif letra== "}":
               q2(letra)
          elif letra == "-":
               q3(letra)
          elif letra == "'":
               q5(letra)
          elif letra == "(":
               q6(letra)
          elif letra == "{":
               q7(letra)
          elif letra== "<":
               q9(letra)
          elif letra== ",":
               q12(letra)
          elif letra == ";":
               q14(letra)
          elif letra== ")":
               q15(letra)
          elif letra== "=":
               q16(letra)
          elif letra== "+": #caso seja um fim de arquivo, vai para estado 21
               q21(letra)
          else:
               showErro(letra) #caso nenhuma das opções, mostra erro"
     else:
          showErro(letra) #caso não seja um caracter válido, mostra erro

#---------------------------------------------------

#------------= Q1 =-------------------------------------------

def q1(letra):
     #print "q1:"+letra
     tokens.append({'nome':'AND','linha':linhas, 'coluna':colunas})
     exit

#------------= Q2 =-------------------------------------------


def q2(letra):
     tokens.append({'nome':'CHD','linha':linhas, 'coluna':colunas})
     exit

#------------= Q3 =-------------------------------------------

def q3(letra):
     letra = proximaletra()
     #print "q3:"+letra
     if is_valido(letra):
          if letra == ">":
               q4(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

#------------= Q4 =-------------------------------------------

def q4(letra):
     letra = proximaletra()
     #print "q4:"+letra
     if is_valido(letra):
          tokens.append({'nome':'IMP','linha':linhas, 'coluna':colunas})
          exit
     else:
          showErro(letra)
#---------------------------------------------------

def q5(letra):
     #print "q5:"+letra
     tokens.append({'nome':'NOT','linha':linhas, 'coluna':colunas})
     exit

#---------------------------------------------------
def q6(letra):
     #print "q6:"+letra
     tokens.append({'nome':'PAE','linha':linhas, 'coluna':colunas})
     exit

#---------------------------------------------------

def q7(letra):
     #print "q7:"+letra
     tokens.append({'nome':'CHE','linha':linhas, 'coluna':colunas})
     exit
#---------------------------------------------------

def q9(letra):
     letra = proximaletra()
     #print "q9:"+letra
     if is_valido(letra):
          if letra == "-":
               q10(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

#---------------------------------------------------

def q10(letra):
     letra = proximaletra()
     #print "q10:"+letra
     if is_valido(letra):
          if letra == ">":
               q11(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

#---------------------------------------------------

def q11(letra):
     letra = proximaletra()
     #print "q11:"+letra
     if is_valido(letra):
          tokens.append({'nome':'EQU','linha':linhas, 'coluna':colunas})
          exit
     else:
          showErro(letra)
#---------------------------------------------------

def q12(letra):
     tokens.append({'nome':'VIR','linha':linhas, 'coluna':colunas})
     exit
#---------------------------------------------------

def q14(letra):
     tokens.append({'nome':'PTV','linha':linhas, 'coluna':colunas})
     exit
#---------------------------------------------------

def q15(letra):
     tokens.append({'nome':'PAD','linha':linhas, 'coluna':colunas})
     exit

#---------------------------------------------------

def q16(letra):
     letra = proximaletra()
     #print "q16:"+letra
     if is_valido(letra):       #caso seja um cacacter valido, se for igual a ":", vai para estado q17, caso nao for ":" é erro!
          if letra == ":":
               q17(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)    #caso nao seja um caracter válido, motra erro!

#---------------------------------------------------
def q17(letra):
     letra = proximaletra()
     #print "q17:"+letra
     if is_valido(letra):
          if letra == "=":
               q18(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)
#---------------------------------------------------
def q18(letra):          #achou uma atribuição =:= , caso o proximo caracter seja valido, gera o token
     letra = proximaletra()
     #print "q18:"+letra
     if is_valido(letra):
          tokens.append({'nome':'ATR','linha':linhas, 'coluna':colunas})
          exit
     else:
          showErro(letra)   #caso seja um caracter invalido, mostra erro!

#---------------------------------------------------
def q19(letra):
     global palavra, aux
     palavra += letra  #concatena segundo caracter
     letra = proximaletra() #pega proximo caracter
     #print letra
     if is_valido(letra):  #testa se é válido
          if (is_letra(letra) or is_numero(letra)): #testa se é uma letra ou um numero
               palavra += letra #concatena proxima letra
               while True:  #vai pegando proximas letras até achar um caracter que nao seja um numero ou uma letra
                    letra = proximaletra()
                    if (not is_letra(letra) and not is_numero(letra)):

                         q20(letra)  #vai para estado 20, onde deve aceitar o token e salva ultimo caracter
                         break
                    if letra != " ":  #nao concatena espaços
                         palavra += letra
                         #print palavra
                         #print letra

          else:   #caso seja valido e nao seja uma letra ou um "numero", podera ser "V", "v", "1","0"...
               q20(letra)
     else:
          showErro(letra) #caso caracter nao seja válido, erro!

#---------------------------------------------------
def q20(letra):
     global palavra, aux, flagVariavel
     if palavra=='V':
          tokens.append({'nome':'TRU','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif palavra=='v':
          tokens.append({'nome':'OR','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif palavra=='1':
          tokens.append({'nome':'TRU','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif palavra=='0':
          tokens.append({'nome':'FAL','linha':linhas, 'coluna':colunas})
          palavra=""
          exit

     elif "Read" == palavra:
          tokens.append({'nome':'REA','linha':linhas, 'coluna':colunas}) #caso a palavra concatenada seja "Read", adiciona a lista e zera a variavel palavra
          palavra=""
          exit
     elif "Print" == palavra:
          tokens.append({'nome':'PR','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif "true" == palavra:
          tokens.append({'nome':'TRU','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif "false" == palavra:
          tokens.append({'nome':'FAL','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif "if" == palavra:
          tokens.append({'nome':'IF','linha':linhas, 'coluna':colunas})
          palavra=""
          exit
     elif "else" == palavra:
          tokens.append({'nome':'ELS','linha':linhas, 'coluna':colunas})
          palavra=""
          exit

     else:
          tokens.append({'nome':'VAR','linha':linhas, 'coluna':colunas}) #caso nao seja nenhuma das palavras anteriores, é uma variavel
          palavra=""
          aux.append(letra) #salva ultimo caracter e seta flag true, para que possa ser avaliado na proxima vez.
          flagVariavel = True
          exit
#---------------------------------------------------
def q21(letra):
     tokens.append({'nome':'+','linha':linhas, 'coluna':colunas})  #final de arquivo
     exit
def getErrolexico():  #se houver um erro lexico...
     return erroLexico

def showTokens(lista_token):
     print "Lista de Tokens:", lista_token



def le_token(): #funcao principal
     global flagVariavel,letra
     if lista_de_caracteres or aux:

          if flagVariavel == True: #caso tenha achado uma variavel por ultimo, pega ultimo caracter lido
               letra = aux.pop()
               flagVariavel=False #seta flag false
          else:
               letra=proximaletra() #se nao, pega proximo caracter da lista referente aso caracteres do arquivo
          q0(letra)
          if tokens:
               return tokens.pop() #reorna token que foi armazenado nesta lista
     else:
          return "Acabou os tokens! :/"

def getErrolexico():
     return erroLexico


#le_token()

#--------------------------INTERFACE ---------------------------------------
def abrirarquivo():
    global arquivo2
    name= askopenfilename(filetypes=[("Text files","*.txt")])
    print name.encode('utf-8')
    arquivo2=name
    abre()

def sobre():
    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height=20, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = "Trabalho de Linguagens Formais!"
    T.insert(END, quote)
    root.title('Sobre')

def abre():
    global arquivo
    arquivo = open(arquivo2)
    conteudo_texto = arquivo.read()
    root = Tk()
    S = Scrollbar(root)
    T = Text(root, height=30, width=50) #,bg='black',fg='white'
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = conteudo_texto
    T.insert(END, quote)
    root.title('Codigo Entrada')
    mainloop()

def AskYesNo(title='Tudo certo!', message='Sucesso!! Deseja ver tokens?'):
        return tkMessageBox.askyesno( title, message )

def analisador():
    global arquivo
    global erroLexico
    global arquivo2
    global lista_token
    global token
    global linhas, colunas

    arquivo = open(arquivo2)
    erroLexico = False

    while True:
        conteudo_texto = arquivo.read(1)
        print conteudo_texto
        lista_de_caracteres.append(conteudo_texto)
        if conteudo_texto == '':
            lista_de_caracteres.append("+")
            lista_de_caracteres.reverse()
            print "Caracteres carregados com sucesso!: ",lista_de_caracteres
            break

    while erroLexico==False:

          token_salvar = le_token()
          if erroLexico==True:
               break
          lista_token.append(token_salvar['nome'])
          if token_salvar['nome'] == "+":
               showTokens(lista_token)
               print lista_token


               #tokens.reverse()
               break

    if erroLexico==False:

          texto = "TUDO CERTO!!"
          if AskYesNo()==True:
               print lista_token
               #tkMessageBox.showinfo("Tokens",lista_token)
               root = Tk()
               S = Scrollbar(root)
               T = Text(root, height=30, width=50)
               S.pack(side=RIGHT, fill=Y)
               T.pack(side=LEFT, fill=Y)
               S.config(command=T.yview)
               T.config(yscrollcommand=S.set)

               T.insert(END, lista_token)
               while len(lista_token) > 0 : lista_token.pop()
               while len( lista_de_caracteres) > 0 :  lista_de_caracteres.pop()
               linhas =1
               colunas =1
               root.title('Tokens')
               mainloop()
    else:
         arquivo = open("log.txt")
         texto = arquivo.read()
         tkMessageBox.showerror("Erro Lexico",texto)
         while len(lista_token) > 0 : lista_token.pop()
         while len( lista_de_caracteres) > 0 :  lista_de_caracteres.pop()
         linhas =1
         colunas =1
         #root = Tk()
         #S = Scrollbar(root)
         #T = Text(root, height=30, width=50,bg='black',fg='red' )



def janela(toplevel):
        Label(text='ANALISADOR LEXICO',font=('Verdana','15','bold')).pack(side=TOP,padx=10,pady=10)

        #Button(text='Abrir', height=1, width=15, command=abrirarquivo).pack()

        fr1 = Frame(toplevel)
        fr1.pack()
        icone1 = PhotoImage(file='icones/abrir.png')
        icone2= PhotoImage(file='icones/analisar.png')
        icone3= PhotoImage(file='icones/sobre.png')
        icone4= PhotoImage(file='icones/sair.png')
        botao0 = Button(fr1,text='Abrir',image=icone1,command=abrirarquivo)
        botao0.image=icone1
        botao0['font']=('Verdana','10')
        #botao0['height']=1
        #botao0['width']=15
        #botao0['image']=icon
        #botao0["background"] = "blue"
        botao0.pack(pady=10)


        botao1 = Button(fr1,text='Analisar',image=icone2,command=analisador)

        botao1.image=icone2
        botao1['font']=('Verdana','10')
        #botao1['height']=1
        #botao1['width']=15
        botao1.pack(pady=10)

        botao2 = Button(fr1, text='Sobre',image=icone3, command=sobre, font=('Verdana','10'))
        botao2.image=icone3
        #botao2['width']= 15
        #botao2['height']=1
        botao2.pack(pady=10)

        botao3 = Button(fr1, text='Sair', image=icone4, command=root.destroy, font=('Verdana','10'))
        botao3.image=icone4
        #botao3['width']= 15
        #botao3['height']=1
        botao3.pack(pady=10)

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir",font=8, command=abrirarquivo)
        filemenu.add_command(label="Analisar",font=8, command=analisador)
        filemenu.add_command(label="Sobre",font=8, command=sobre)

        filemenu.add_separator()
        filemenu.add_command(label="Sair",font=8, command=root.destroy)
        menubar.add_cascade(label="Arquivo",font=8, menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_separator()
        #menubar.add_cascade(label="Sobre",font=8, menu=editmenu, command=sobre)
        #helpmenu = Menu(menubar, tearoff=0)
        #menubar.add_cascade(label="Ajuda",font=8, menu=helpmenu)
        root.config(menu=menubar)
        root.title('Analisador Lexico')

root = Tk()
#root.geometry("1800x1600")
root.geometry("300x450")
janela(root)
root.mainloop()

