from tkinter import *
from random import *
from tkinter import messagebox
from pygame import mixer
from interfaceConexao import *

inter = interface()

# ------------------------------------------- INICIO DAS CONFIGURAÇÕES DO FORMULÁRIO -------------------------------------------

#Config da Janela
janela = Tk()
janela.geometry('1000x600')
janela.title('JOGO DO BIXÃO 3.0 -- TESTE TODOS CONHECIMENTOS E FIQUE RICO :° ')
janela.resizable(0,0)
janela['bg'] = '#696969'

#Saldo Aleatorio
saldoAleatorio = float(randint(99,150))

#nome do Usuario
arqNomeTemp = open('nomeTemp.txt','r')
nomeUser = ''

for i in arqNomeTemp:
    nomeUser = i

# ----------------------------------------- MENSAGEM DE INICIO PARA O USER -----------------------------------------
messagebox.showinfo('BEM VINDO AO SHOW DO BIXÃO','OLÁ,{}\nVOCÊ TERÁ QUE RESPONDER PERGUNTAS DE ASSUNTOS VARIADOS:\n\nCADA ACERTO VALERÁ, QUANTIDADE DE QUESTÕES CORRETAS VEZES 1000\n\n SEU SALDO: R$ 1000,00\n\n\n<.: BOA SORTE :.>'.format(nomeUser))

#chamar a musica de fundo
def Musica():
    mixer.init()
    mixer.music.load('musica.mp3')
    mixer.music.play()

Musica()

#Labels
lblPergunta = Label(text='0', font='Courier 12 bold', fg='yellow', bg='#696969')
lblPergunta.pack()
#lblPergunta.place(x=10,y=10)

#LAbels de Alternativas
lblA = Label(text='', bg='#696969', font='Courier 22 bold')
lblA.place(x=120,y=120)

lblB = Label(text='', bg='#696969', font='Courier 22 bold')
lblB.place(x=120,y=210)

lblC = Label(text='', bg='#696969', font='Courier 22 bold')
lblC.place(x=120,y=290)

lblD = Label(text='', bg='#696969', font='Courier 22 bold')
lblD.place(x=120,y=370)

#Saldo
lblReais = Label(text='R$', bg='#696969', font='Courier 18 bold', fg='white')
lblReais.place(x=790,y=550)

lblSaldo = Label(text='1000', fg='lime', font='Courier 24 bold', bg='#696969')
lblSaldo.place(x=855,y=550)

#Respota Correta para Comparar
RespotaCorreta = []

#lista de Indices de Perguntas
lista = [n for n in range(1,31)]

#lista de Acertos e Erros
listaAcertosErros = [0,0]

#Botoes
btA = Button(text='A', command=lambda: verficarResposta('A'), fg='white', bg='black', font='Courier 24 bold')
btA.place(x=50,y=115)

btB = Button(text='B', command=lambda: verficarResposta('B'), fg='white', bg='black', font='Courier 24 bold')
btB.place(x=50,y=205)

btC = Button(text='C', command=lambda: verficarResposta('C'), fg='white', bg='black', font='Courier 24 bold')
btC.place(x=50,y=285)

btD = Button(text='D', command=lambda: verficarResposta('D'), fg='white', bg='black', font='Courier 24 bold')
btD.place(x=50,y=365)

#Para agora
def desistir():
    
    if str(saldoAleatorio) == lblSaldo['text']:
        messagebox.showerror('','SEU SALDO TEM QUE SER MAIOR OU MENOR AO INICIAL, VAMOS TER CONTINUAR .... :)')

    else:
        mensagemEndGame()
        janela.destroy()
        
btDesistir = Button(text='Prefiro parar AGORA !', fg='white', background='red', font='Courier 12 bold', command=desistir)
btDesistir.place(x=20,y=550)

#Verifica Resposta
def verficarResposta(rUser):

    janelaAtiva = True
    
    if rUser == RespotaCorreta[-1]:
        messagebox.showinfo('BEM DEMAIS :0','Parabéns Você Acertou :)')
        
        #Soma a quantidade de acertos a posicao 0 da lista
        listaAcertosErros[0] += 1

        #modifica o saldo
        setSaldo(True)
        
    else:
        #setSaldo(False)

        #Som de Erro
        mixer.music.load('Errou.mp3')
        mixer.music.play()
        
        messagebox.showerror('NÃO FOI DESSA VEZ ;-;',' Errouuuuuuuuuuuuuuuuuuuuuuuuuuuu :(')

        #Me
        janelaAtiva = False

        #Exibir a mensagem de Fim de Jogo
        mensagemEndGame()

        #Destruir Janela
        janela.destroy()
        
        #Soma a quantidade de erros a posicao 1 da lista
        #listaAcertosErros[1] += 1

        #chamar musica de fundo
        #Musica()
    
    #Caso a janela inda exista, Pegar uma nova Pergunta
    if janelaAtiva:
        getPerguntaR()
    
#Modificar Pergunta
def setPergunta(texto):
    lblPergunta['text'] = texto

#pegar a pergunta, alternativas e a resposta correta
def getPerguntaR():

    #caso não exista Nenhum elemento na lista
    if len(lista) == 0:
        mensagemEndGame()

    else:
        #Escolher um elemento da lista e remove-lo
        elemento = choice(lista)
        lista.remove(elemento)
        
        #arqPerg = open(r'C:\\Users\\Igor Santos\\Documents\\PeR\\Pergunta{}.txt'.format(str(elemento)),'r', encoding='latin-1')
        arqPerg = open('Pergunta{}.txt'.format(str(elemento)),'r', encoding='latin-1')

        for pos,i in enumerate(arqPerg):
            #envia a pergunta
            if pos == 0:
                setPergunta(i)
                
            #Modifica o texto de cada Letra
            elif pos == 1:
                lblA['text'] = i
            elif pos == 2:
                lblB['text'] = i
            elif pos == 3:
                lblC['text'] = i
            elif pos == 4:
                lblD['text'] = i
                
            #Salva a resposta Correta
            elif pos == 5:
                RespotaCorreta.append(i)

        arqPerg.close()

def setSaldo(status):
    
    novoSaldo = ''
    saldoAntigo = lblSaldo['text']
    
    #converte o saldo antigo para FLOAT
    saldoFloat = float(saldoAntigo)

    #Caso o USER acerte soma quantidadeAcertos * 1000
    if status:
        novoSaldo = str(listaAcertosErros[0] * (saldoFloat + 1000))

    #modifica o texto do Saldo
    lblSaldo['text'] = novoSaldo
    
def mensagemEndGame():
    #Atributos
    dinheiro = str(float(lblSaldo['text']) / 2)
    acertos = listaAcertosErros[0]
    
    #Quando o jogo acaba
    mixer.music.stop()
    mensagem = 'O JOGO ACABOU :(\n\n\nSEU DINHEIRO: R$ {}\n\nQUANTIDADE DE ACERTOS: {}\n\n\n\n<...: OBRIGADO POR JOGAR, VOLTE SEMPRE :) :...>'.format(dinheiro,acertos)
    messagebox.showinfo('END GAME',mensagem)

    #adicionarUsuario ao Rank
    inter.setRanking(nomeUser, dinheiro)


#inicia com a primeira Pergunta
getPerguntaR()

janela.mainloop()
