def verificar_paridade(numero):
    """Função que verifica se um número é par ou ímpar."""
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

matriculas = []

while len(matriculas) < 5:
    try:
        numero = int(input("Insira o número de matrícula: "))
        matriculas.append(numero)
    except ValueError:
        print("Por favor, insira um número válido.")

for numero in matriculas:
    resultado = verificar_paridade(numero)
    print(f"O número {numero} é {resultado}.")
