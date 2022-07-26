import random
from tkinter import *
root= Tk()
root.title('cripto foda')
root.geometry('200x250')
valor = 0


def cripto(mensagem, chave):
    mensagem = list(mensagem)
    random.seed(chave)
    for i in range(len(mensagem)):
        mensagem[i] = ord(mensagem[i])
        mensagem[i]+=random.randint(1,45)
        mensagem[i] = chr(mensagem[i])
    mensagem = ''.join(mensagem)
    return mensagem
    
def descripto(mensagem, chave):
    mensagem = list(mensagem)
    random.seed(chave)
    for i in range(len(mensagem)):
        mensagem[i] = ord(mensagem[i])
        mensagem[i]-=random.randint(1,45)
        mensagem[i] = chr(mensagem[i])
    mensagem = ''.join(mensagem)
    return mensagem

def main():
    cifra = slider.get()
    mensagem = texto.get()
    if not valor:
        mensagem_nova = descripto(mensagem, cifra)
        
    else:
        mensagem_nova = cripto(mensagem, cifra)
    resultado.delete(0, END)
    resultado.insert(0, mensagem_nova)

def radio1():
    global valor
    valor = 0
def radio2():
    global valor
    valor = 1
    
criptografar = IntVar()

opcao = LabelFrame(root, text = 'Opção')
radio_cripto = Radiobutton(opcao, text = 'Criptografar', variable = criptografar, value = 0, command = radio1)
radio_descripto = Radiobutton(opcao, text = 'Descriptografar', variable = criptografar, value = 1, command = radio2)
num_cifra = LabelFrame(root, text = 'Cifra')
Entrada = LabelFrame(root, text='Entrada')
texto= Entry(Entrada)
saída=LabelFrame(root, text='Resultado')
botao=Button(root, text='Converter', command=main)
slider=Scale(num_cifra, from_=1, to=50, orient=HORIZONTAL)
resultado=Entry(saída)

texto.pack()
Entrada.pack()
num_cifra.pack()
slider.pack()
opcao.pack()
radio_cripto.pack(anchor = W)
radio_descripto.pack(anchor = W)
botao.pack()
saída.pack()
resultado.pack()

mainloop()

""" for i in range(30):
    a = descripto('iaflyyrs gjxbvfuy',i)
    print(f'chave({i}) - {a}') """