# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Insira o valor do ângulo'))

angulorad = math.radians(angulo)

print(f"""O seno de {angulo} é: {math.sin(angulorad):.2f} 
O cosseno de {angulo} é: {math.cos(angulorad):.2f} 
A tangente de {angulo} é: {math.tan(angulorad):.2f}
""")