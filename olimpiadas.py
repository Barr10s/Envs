def determinar_grupo(matricula):
    if matricula % 2 == 0:
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:
        return "VOCÊ ESTÁ NO TIME AMARELO"

numero_matricula = int(input("Digite o número da sua matrícula: "))
mensagem = determinar_grupo(numero_matricula)
print(mensagem)
