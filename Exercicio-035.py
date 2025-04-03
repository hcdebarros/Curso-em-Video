# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

ladoa = float(input("Insira a medida do lado A"))
ladob = float(input("Insira a medida do lado B"))
ladoc = float(input("Insira a medida do lado C"))


if ladoa + ladob <= ladoc:
    print("Não é um triângulo")
    exit()

if ladoa + ladoc <= ladob:
    print("Não é um triângulo")
    exit()

if ladob + ladoc <= ladoa:
    print("Não é um triângulo")
    exit()

if ladoa == ladob == ladoc:
    print("É um triângulo equilátero")

elif ladoa == ladob or ladoa == ladoc or ladoc == ladob:
    print("É um triângulo isoscéles")

else:
    print("É um triângulo escaleno")