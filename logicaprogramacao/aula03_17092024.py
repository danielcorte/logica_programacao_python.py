"""6 - Conversor de Unidades. Escreva um programa que permite ao usuário escolher
entre converter uma temperatura de Celcius para Fahrenheit ou vice-versa. Solicite o valor
e execute a conversão.

print("-" * 20, "\n  BEM-VINDO\n", "-" * 20, "\n[1] - Converter para Fahrenheit\n[2] - Converter para Celcius")
print("-" * 20)
escolha = int(input("O que você deseja?: "))
if escolha == 1:
    temp = float(input("Digite em Celcius o valor para ser convertido °C:"))
    resultado = (temp * 9/5) + 32
    print("-" * 20)
    print(f"\n{temp}°C = {resultado}°F")
elif escolha == 2:
    temp = float(input("Digite em Fahrenheit o valor para ser convertido °F:"))
    resultado = (temp - 32) / 1.8
    print("-" * 20)
    print(f"{temp}°F = {resultado}°C")
else:
    print("Opção inválida!")
print("-" * 20)"""

"""7 - Verificação de Triângulo. Crie um programa que solicita três comprimentos e determina se esses comprimentos 
podem formar um triângulo. Se sim, classifique-o como equilátero, isósceles ou escaleno

print("-" * 40)
print("CRIADO E VERIFICADOR DE TRIANGULOS")
print("-" * 40)
primeiro_lado = float(input("Digite o tamanho do primeiro lado do triângulo (m): "))
print("-" * 40)
segundo_lado = float(input("Digite o tamanho do segundo lado do triângulo (m): "))
print("-" * 40)
terceiro_lado = float(input("Digite o tamanho do terceiro lado do triângulo (m): "))
print("-" * 40)

if primeiro_lado + segundo_lado > terceiro_lado and segundo_lado + terceiro_lado > primeiro_lado and terceiro_lado + primeiro_lado > segundo_lado:
    if primeiro_lado == segundo_lado == terceiro_lado:
        print("Esse triângulo é equilátero")

    elif primeiro_lado == segundo_lado or segundo_lado == terceiro_lado or terceiro_lado == primeiro_lado:
        print("Esse triângulo é isósceles")

    elif primeiro_lado != segundo_lado != terceiro_lado:
        print("Esse triângulo é escaleno")
else:
    print(f"É impossível formar um triângulo com esssas medidas")"""

"""8 - Crie um programa em python """

"""9 - Jogo de Pedra, Papel e Tesoura. Crie um jogo de Pedra, Papel e Tesoura em que o usuário jogue contra o computador
import random

print("-" * 40)
print("  PEDRA | PAPEL | TESOURA")
print("-" * 40)
jogada_pc = random.choice(["pedra", "papel", "tesoura"])
jogada_user = str(input("Escolha entre 'pedra', 'papel' e 'tesoura': "))
print(f"Sua jogada: {jogada_user}")
print(f"Jogada do PC: {jogada_pc}")
print("-" * 40)

if jogada_pc == jogada_user:
    print("Resultado: EMPATE!!!")

if jogada_pc == 'pedra' and jogada_user == 'tesoura' or jogada_pc == 'tesoura' and jogada_user == 'papel' or jogada_pc == 'papel' and jogada_user == 'pedra':
    print("Resultado: DERROTA!!!")

if jogada_user == 'pedra' and jogada_pc == 'tesoura' or jogada_user == 'tesoura' and jogada_pc == 'papel' or jogada_user == 'papel' and jogada_pc == 'pedra':
    print("Resultado: VITORIA!!!")"""