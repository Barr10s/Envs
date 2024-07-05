import requests

integrantes = {
    'Murillo': '11629-224',
    'Lucila': '12410-010',
    'Daniel': '11089-050',
}

def obter_cidade_por_cep(cep):
    respostas = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if respostas.status_code == 200:
        dados = respostas.json()
        return dados.get('localidade')
    return None

for nome, cep in integrantes.items():
    cidade = obter_cidade_por_cep(cep)
    if cidade:
        print(f'Nome: {nome}, Cidade: {cidade}')
    else:
        print(f'Nome: {nome}, Cidade: Não encontrada')