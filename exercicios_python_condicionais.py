# -*- coding: utf-8 -*-
"""Exercicios Python - Condicionais

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1whqcjqW2qbmNGXrf1AfYMCKv4pNyidwy
"""

#Programa que peça a idade da pessoa e imprima se ela é maior ou menor de 18 anos.

idade = int(input("Digite sua idade: "))

if (idade >= 18):
  print("Maior de idade")
else:
  print("Menor de idade")

#Programa que peça um número e mostre se ele é positivo ou negativo.

numero = float(input("Digite seu numero: "))

if (numero > 0):
  print("Numero positivo")
elif (numero == 0):
  print("Neutro")
else:
  print("Numero negativo")

primeiro_numero = float(input("digite um numero: "))
segundo_numero = float(input("digite um numero: "))

if (primeiro_numero > segundo_numero):
  print(f"{primeiro_numero} é maior do que {segundo_numero}.")

elif (primeiro_numero == segundo_numero):
  print(f"Os numeros são iguais.")

else:
  print(f"{segundo_numero} é maior do que {primeiro_numero}.")

#Programa que peça a nota de 3 provas de um aluno e mostre se ele passou ou não de ano.
#O aluno irá passar de ano se a média das suas notas for maior ou igual a 6 (média é a soma das notas dividido pelo número de provas).

nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3
media = round(media,2)


if (media >= 6):
  print(f"{media}: APROVADO")
else:
  print(f"{media}: REPROVADO")

# Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e). Sabendo a resposta certa, 
# o programa deve receber a opção do usuário e informar a letra que o usuário marcou e se a resposta está certa ou errada.
# resposta certa = c

print("Qual a raiz quadrada de de 729?")

print("a)23 b)29 c)27 d)33 e)19")

resposta = input("Qual letra está correta?: ")
resposta_correta = "c"

if (resposta == resposta_correta ):
  print("A resposta está correta")
else:
  print(f"Resposta incorreta, a resposta é letra {resposta_correta}, 27")

#Fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino,
#a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

#a. Mora perto da vítima?
#b. Já trabalhou com a vítima?
#c. Telefonou para a vítima?
#d. Esteve no local do crime?
#e. Devia para a vítima?

#Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos 
#são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
#necessitando outras investigações. Valores abaixo de 1 são liberados.

print("RESPONDA 1 PARA SIM, 0 PARA NÃO")

res_1 = int(input("Mora perto da vítima?: "))
res_2 = int(input("Já trabalhou com a vítima?: "))
res_3 = int(input("Telefonou para a vítima?: "))
res_4 = int(input("Esteve no local do crime?: "))
res_5 = int(input("Devia para a vítima?: "))

soma_res = res_1 + res_2 + res_3 + res_4 + res_5

if(soma_res == 3 or soma_res == 4 ):
  print("Cumplice") 
elif(soma_res == 5):
  print("Assassino")
elif(soma_res == 2):
  print("Suspeito")
else:
  print("Liberado, é necessário novas investigações" )

#incompleto
import random

numero = int(input("Digite seu numero: "))

#Vamos fazer um radar eletrônico de velocidade. Faça um programa que leia a velocidade de um carro, 
#e diga se ele está acima ou não da velocidade permitida de 50 km/h. Se o carro estiver acima da velocidade,
#o programa deve imprimir que o motorista ultrapassou a velocidade permitida e recebeu uma multa num determinado valor. 
#Para calcular o valor da multa, considere que
#para cada quilômetro acima da velocidade permitida, 
#o motorista deve pagar 10 reais.

velocidade_limite = 50
velocidade_carro = float(input("Qual foi a velocidade do carro?: "))
excesso = velocidade_carro - velocidade_limite
multa = (excesso*10)


if (velocidade_carro == velocidade_limite):
  print("Velocidade máxima permitida")
elif(velocidade_carro > velocidade_limite):
  print(f"Está acima do limite estabelecido, com o excesso de {excesso} km/h e deverá pagar a multa de {multa} reais")
else:
  print("Dentro da normalidade")

#Com a recomendação que as pessoas fiquem em casa e evitem aglomerações como medida pra frear a contaminação pelo coronavírus, 
#como saber quando devemos procurar um hospital? Faça um programa que pergunte os sintomas que
#a pessoa apresenta e responda se ela deve ou não procurar um hospital.

#Sintomas: a. Você tem febre persistente? b. Você tem dificuldade para respirar?
#A resposta do programa deve seguir a seguinte tabela:

#A	B	Resultado
#Sim	Não	Fique em casa
#Não	Sim	Fique em casa
#Não	Não	Fique em casa
#Sim	Sim	Procure um hospital

print("Responda com s para sim e n para não")

a = input("Você tem febre persistente?: ")
b = input("Você tem dificuldade de respirar?: ")

if(a == "s" and b == "s"):
  print("Procure um hospital")

else: 
  print("Fique em casa")

from random import randrange


numero = int(input("Digite um número: "))
numero_aleatorio = random.sample(range(100), 3)

if (numero == numero_aleatorio):
  print("Você Acertou.")
else:
  print("Você errou")