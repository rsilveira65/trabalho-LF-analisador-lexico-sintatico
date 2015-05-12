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

#Conjunto dos simbolos não reservados em Q0 ex: if "i" é reservado, por isso não está aqui
naoreservado= ["z","b","_","c", "d","f","g","h","j","k","l","m","n","o","a","p","q","r","s","t","u","x","w","y","z"]

alfabeto = ["z","a","A","b","B","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","v","X","Y","y","x","W","w","Z","z"]
numeros = ["z","0","1","2","3","4","5","6","7","8","9"]

#Conjunto de todos simbolos validos
valido =["z","_"," ","","0","F","V","1","2","3","4","5","6","7","8","9","a","^","'","a","A","b","B","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","v","X","Y","y","x","W","w","Z","z",",","'","-",";",":","(",")","{","}",""," ","-","\t","\r","\b","R","P","T"," F ","<",">","=","w"]
linhas =1
colunas =1
erroLexico = True

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
def showErro(letra):
     global fileb
     global linhas
     global erroLexico
     erroLexico = False

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
     letra = arquivo.read(1)
     if letra =="\n":
          linha=incLinha_Coluna(1)
          letra = arquivo.read(1)
     incLinha_Coluna(0)
     return letra

#------------= Q0 =-------------------------------------------

def q0(letra):
     if is_valido(letra):
          #print "q0:"+letra
          if letra == "F":
               q44(letra)
          elif letra == "V":
               q25(letra)
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
          elif letra == "v":
               q41(letra)
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
          elif letra == "R":
               q7(letra)
          elif letra == "T":
               q16(letra)
          elif letra== "P":
               q11(letra)
          elif letra== "e":
               q3(letra)
          elif letra == "i":
               q1(letra)
          elif letra == "":
               exit
          elif letra == " ":
               exit
          elif (is_naoReservado(letra))==True:
               q20(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

#------------= Q1 =-------------------------------------------

def q1(letra):
     letra = proximaletra()
     #print "q1:"+letra
     if is_valido(letra):
          if letra == "f":
               q2(letra)
     else:
          showErro(letra)

#------------= Q2 =-------------------------------------------

def q2(letra):
     letra = proximaletra()
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               q20(letra)
          else:
               tokens.append("if")
               q0(letra)
     else:
          showErro(letra)

#------------= Q3 =-------------------------------------------

def q3(letra):
     letra = proximaletra()
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               if letra=="l":
                    q4(letra)
               else:
                    q20(letra)
          else:
               tokens.append("Identificador")
               q0(letra)
     else:
          if letra == None:
               tokens.append("Identificador")
               q0(letra)

          else:
               showErro(letra)

#------------= Q4 =-------------------------------------------

def q4(letra):
     letra = proximaletra()
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               if letra=="s":
                    q5(letra)
               else:
                    q20(letra)
          else:
               tokens.append("Identificador")
               q0(letra)

     else:
          if letra == None:
               tokens.append("Identificador")
               q0(letra)

          else:
               showErro(letra)

#------------= Q5 =-------------------------------------------

def q5(letra):
     letra = proximaletra()
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               if letra=="e":
                    q6(letra)
               else:
                    q20(letra)
          else:
               tokens.append("Identificador")
               q0(letra)

     else:
          if letra == None:
               tokens.append("Identificador")
               q0(letra)

          else:
               showErro(letra)

#------------= Q6 =-------------------------------------------

def q6(letra):
     letra = proximaletra()
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               q20(letra)
          else:
               tokens.append("else")
               q0(letra)
     else:
          showErro(letra)

#------------= Q7 =-------------------------------------------

def q7(letra):
     letra = proximaletra()
     #print "q7:"+letra
     if is_valido(letra):
          if letra == "e":
               q8(letra)
          else:

               showErro(letra)
     else:

          showErro(letra)

#------------= Q8 =-------------------------------------------

def q8(letra):
     letra = proximaletra()
     #print "q8:"+letra
     if is_valido(letra):
          if letra == "a":
               q9(letra)
          else:

               showErro(letra)
     else:

          showErro(letra)

#------------= Q9 =-------------------------------------------

def q9(letra):
     letra = proximaletra()
     #print "q9:"+letra
     if is_valido(letra):
          if letra == "d":
               q10(letra)
          else:

               showErro(letra)
     else:

          showErro(letra)

#------------= Q10 =-------------------------------------------

def q10(letra):
     letra = proximaletra()
     #print "q10:"+letra
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               showErro(letra)
          else:
               tokens.append("Read")
               q0(letra)
     else:
          showErro(letra)

#------------= Q11 =-------------------------------------------

def q11(letra):
     letra = proximaletra()
     #print "q11:"+letra
     if is_valido(letra):
          if letra == "r":
               q12(letra)
     else:
          showErro(letra)

#------------= Q12 =-------------------------------------------

def q12(letra):
     letra = proximaletra()
     #print "q12:"+letra
     if is_valido(letra):
          if letra == "i":
               q13(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

 #------------= Q13 =-------------------------------------------

def q13(letra):
     letra = proximaletra()
     #print "q13:"+letra
     if is_valido(letra):
          if letra == "n":
               q14(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

 #------------= Q14 =-------------------------------------------

def q14(letra):
     letra = proximaletra()
     #print "q14:"+letra
     if is_valido(letra):
          if letra == "t":
               q15(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

 #------------= Q15 =-------------------------------------------

def q15(letra):
     letra = proximaletra()
     #print "q15:"+letra
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
              showErro(letra)
          else:
               tokens.append("Print")
               q0(letra)
     else:
          showErro(letra)

 #------------= Q16 =-------------------------------------------

def q16(letra):
     letra = proximaletra()
     #print "q16:"+letra
     if is_valido(letra):
          if letra == "r":
               q17(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

def q17(letra):
     letra = proximaletra()
     #print "q17:"+letra
     if is_valido(letra):
          if letra == "u":
               q18(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

def q18(letra):
     letra = proximaletra()
     #print "q18:"+letra
     if is_valido(letra):
          if letra == "e":
               q19(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

def q19(letra):
     letra = proximaletra()
     #print "q19:"+letra
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               showErro(letra)
          else:
               tokens.append("True")
               q0(letra)
     else:
          showErro(letra)

def q20(letra):
     letra = proximaletra()
     #print "q20: "+letra
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               q43(letra)

          else:
               tokens.append("Identificador")
               q0(letra)
     else:
          if letra == None:
               tokens.append("Identificador")
               exit
          else:
               showErro(letra)

def q21(letra):
     letra = proximaletra()
     #print "q21:"+letra
     tokens.append(" ^ ")
     q0(letra)

def q22(letra):
     letra = proximaletra()
     #print "q22:"+letra
     tokens.append(" , ")
     q0(letra)

def q23(letra):
     letra = proximaletra()
     #print "q23:"+letra
     tokens.append(" ( ")
     q0(letra)

def q24(letra):
     letra = proximaletra()
     #print "q24:"+letra
     tokens.append(" ) ")
     q0(letra)

def q25(letra):
     letra = proximaletra()
     #print "q25:"+letra
     tokens.append(" V ")
     q0(letra)

def q26(letra):
     letra = proximaletra()
     #print "q26:"+letra
     if is_valido(letra):
          if letra == "l":
               q27(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

def q27(letra):
     letra = proximaletra()
     #print "q27:"+letra
     if is_valido(letra):
          if letra == "s":
               q28(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

def q28(letra):
     letra = proximaletra()
     #print "q28:"+letra
     if is_valido(letra):
          if letra == "e":
               q29(letra)
          else:
               showErro(letra)
     else:
          showErro(letra)

def q29(letra):
     letra = proximaletra()
     #print "q29:"+letra
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               showErro(letra)
          else:
               tokens.append("OP_LOGICO")
               q0(letra)
     else:
          showErro(letra)

def q30(letra):
     letra = proximaletra()
     #print "q30:"+letra
     tokens.append(" { ")
     q0(letra)

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
          tokens.append("=:=")
          q0(letra)
     else:
          showErro(letra)

def q34(letra):
     letra = proximaletra()
     #print "q34:"+letra
     tokens.append(" } ")
     q0(letra)

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
          q0(letra)
     else:
          showErro(letra)

def q38(letra):
     letra = proximaletra()
     #print "q38:"+letra
     tokens.append(" ' ")
     q0(letra)

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
          q0(letra)
     else:
          showErro(letra)

def q41(letra):
     letra = proximaletra()
     #print "q41:"+letra
     tokens.append(" v ")
     q0(letra)


def q42(letra):
     letra = proximaletra()
     #print "q42:"+letra
     tokens.append(" ; ")
     q0(letra)


def q43(letra):
     letra = proximaletra()
     #print "q43: "+letra
     if is_valido(letra):
          if (is_letra(letra) or is_numero(letra))==True:
               q20(letra)
          else:
               tokens.append("Identificador")
               q0(letra)
     else:
          if letra == None:
               tokens.append("Identificador")
               exit
          else:
               showErro(letra)

def q44(letra):
     letra = proximaletra()
     #print "q44:"+letra
     if is_valido(letra):
          if letra == "a":
               q26(letra)
          else:
               tokens.append(" F ")
               q0(letra)

     else:
          showErro(letra)

def showTokens(tokens):
     print "Lista de Tokens:", tokens

def preparaLista(tokens):
     global arquivo
     global arquivo2
     arquivo = open(arquivo2)
     while True:

                         letra = proximaletra()
                         q0(letra)

                         if letra == '':
                                   showTokens(tokens)
                                   tokens.reverse()
                                   break

def le_token():
     return tokens.pop()

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
def AskYesNo(title='TUDO CERTINHO QUERIDÃO!', message='Sucesso!! Deseja ver tokens?'):
        return tkMessageBox.askyesno( title, message )

def analisador():
    global arquivo
    global erroLexico
    arquivo = open(arquivo2)
    erroLexico = True

    preparaLista(tokens)
    if getErrolexico()==True:

          texto = "TUDO CERTO!!"
          if AskYesNo()==True:

               tkMessageBox.showinfo("Tokens",tokens)
               root = Tk()
               S = Scrollbar(root)
               T = Text(root, height=30, width=50)
               S.pack(side=RIGHT, fill=Y)
               T.pack(side=LEFT, fill=Y)
               S.config(command=T.yview)
               T.config(yscrollcommand=S.set)
               quote = texto
               T.insert(END, tokens)
               root.title('Tokens')
               mainloop()
    else:
         arquivo = open("log.txt")
         texto = arquivo.read()
         tkMessageBox.showerror("Erro Lexico",texto)
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

