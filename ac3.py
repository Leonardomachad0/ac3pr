#1
def calcular_reajuste_salario(salario):
    if salario <= 280:
        percentual_aumento = 20
    elif salario <= 700:
        percentual_aumento = 15
    elif salario <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = (salario * percentual_aumento) / 100
    novo_salario = salario + aumento

    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")

salario = float(input("Digite o salário do colaborador: "))
calcular_reajuste_salario(salario)


#2
def dia_da_semana(numero):
    if numero == 1:
        return "Domingo"
    elif numero == 2:
        return "Segunda-feira"
    elif numero == 3:
        return "Terça-feira"
    elif numero == 4:
        return "Quarta-feira"
    elif numero == 5:
        return "Quinta-feira"
    elif numero == 6:
        return "Sexta-feira"
    elif numero == 7:
        return "Sábado"
    else:
        return "Valor inválido"

numero = int(input("Digite um número (1 a 7): "))
print(dia_da_semana(numero))

#3
import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")