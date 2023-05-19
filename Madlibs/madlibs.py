# MADLIBS é um "jogo de palavras"
# onde as palavras digitadas preenchem lacunas,
# completando uma frase no final
# é um jogo popular entre crianças, nos EUA

from tkinter import *

# Tk() cria uma janela
game = Tk()
# geometry() sendo utilizado para definir
# tamanho e altura da janela
game.geometry('600x500')
# title() nomeia a janela
game.title('Gerador de Madlibs')
# Label() mostra um texto não modificável
# game é o nome dado à janela
# place() define posição específica
Label(game, text='Gerador de Madlibs \n Divirta-se!',
      font='Arial 20 bold').place(x=160, y=80)


# primeiro madlib definido em uma função


def madlib1():
    pessoaFamosa = input("Insira o nome de uma pessoa famosa: ")
    substantivo = input("Insira um substantivo no plural: ")
    adjetivo = input("Insira um adjetivo: ")
    adjetivo2 = input("Insira um adjetivo: ")
    substantivo2 = input("Insira um substantivo: ")
    adjetivo3 = input("Insira um adjetivo: ")
    lugar = input("Insira um lugar: ")
    adjetivo4 = input("Insira um adjetivo: ")
    substantivo3 = input("Insira um substantivo: ")
    palavra = input("Insira uma palavra aleatória: ")
    açao = input("Insira uma ação sendo realizada: ")
    madlib = f"{pessoaFamosa}, o pai de todos os {substantivo}, era um homem muito {adjetivo}. Quando ele era uma criança {adjetivo2}, ele pegou um(a) {substantivo2} e correu até um(a) {adjetivo3} {lugar}, onde ele encontrou um {adjetivo4} {substantivo3}. '{palavra}, disse ele, {açao}.'"
    print(madlib)

# segundo madlib definido em uma função


def madlib2():
    adjetivo = input("Insira um adjetivo: ")
    cor = input("Insira uma cor: ")
    substantivo = input("Insira um substantivo: ")
    lugar = input("Insira um lugar: ")
    pessoaFamosa = input("Insira o nome de uma pessoa famosa: ")
    animal = input("Insira o nome de um animal: ")
    alimento = input("Insira um alimento: ")
    madlib = f"Na noite passada, eu sonhei que era uma {adjetivo} borboleta com asas de cor {cor} que pareciam com um(a) {substantivo}. Então, eu voei até um(a){lugar} com meu melhor amigo e {pessoaFamosa}, que usava uma camiseta com um(a) {animal} estampado e comia um(a) {alimento}."
    print(madlib)


# terceiro madlib definido em uma função


def madlib3():
    lugar = input("Insira um lugar: ")
    adjetivo = input("Insira um adjetivo: ")
    alimento = input("Insira um alimento: ")
    açao = input("Insira uma ação sendo realizada: ")
    substantivo = input("Insira um substantivo: ")
    madlib = f"Hoje eu fui até o(a) {lugar}, onde colhi um(a) {adjetivo} {alimento}. Meu objetivo era cozinhar um prato de {alimento}, mas fiquei com preguiça e resolvi {açao} com um {substantivo}."
    print(madlib)


# gera os botões para abrir a opção selecionada
Button(game, text='Jogo 1', font='arial 15',
       command=madlib1, bg='ghost white').place(x=250, y=180)
Button(game, text='Jogo 2', font='arial 15',
       command=madlib2, bg='ghost white').place(x=250, y=240)
Button(game, text='Jogo 3', font='arial 15',
       command=madlib3, bg='ghost white').place(x=250, y=300)
game.mainloop()
