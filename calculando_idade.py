# Calculando a idade de uma pessoa
print("xxxxQual sua idadexxxx")
from datetime import datetime

def calcula_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Solicita a data de nascimento do usuário
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Calcula e exibe a idade
idade = calcula_idade(data_nascimento)
print(f"Sua idade é: {idade} anos.")