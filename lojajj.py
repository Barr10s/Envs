import requests

# Definição dos estados das regiões Norte e Nordeste
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
estados_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

def get_estado_por_cep(cep):
    """
    Função que consulta uma API externa para obter o estado a partir do CEP.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return data['uf']
        else:
            return None
    else:
        return None

def verifica_frete_gratis(cep):
    """
    Função que verifica se o CEP está elegível para frete grátis.
    """
    estado = get_estado_por_cep(cep)
    if estado:
        if estado in estados_norte or estado in estados_nordeste:
            return True
        else:
            return False
    else:
        return False

def main():
    cep = input("Digite o CEP (somente números): ")
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. O CEP deve conter 8 dígitos numéricos.")
        return
    
    if verifica_frete_gratis(cep):
        print("Este CEP é elegível para frete grátis!")
    else:
        print("Este CEP não é elegível para frete grátis.")

if __name__ == "__main__":
    main()
