import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dados = pd.read_csv("salaries.csv")

df = pd.DataFrame(dados)

job_title_media = dados.groupby("job_title")["salary_in_usd"].mean()

barra_salarie_per_jobtitle = plt.figure("grafico_de_barras_salarie_per_jobtitle")

job_title_media.plot.bar()

plt.show()

experience_level_media = dados.groupby("experience_level")["salary_in_usd"].mean()

barra_salarie_per_experience_level = plt.figure("grafico_de_barras_salarie_per_experience_level")

experience_level_media.plot.bar()

plt.show()


#jobtitle.hist(bins=2)

#df_media = pd.DataFrame(dados['salary_in_usd'], dados['job_title'])


#df_media.plot.bar()

moda = df['salary_in_usd'].mode().values[0]
print("A moda da coluna é:", moda)

mediana = df['salary_in_usd'].median()
print("A mediana da coluna é:", mediana)

variancia = df['salary_in_usd'].var()
print("A variância da coluna é:", variancia)

quartis = df['salary_in_usd'].quantile([0.25, 0.5, 0.75]).values
print("Quartis da coluna são:", quartis)

curtose = df['salary_in_usd'].kurtosis()
print("A curtose da coluna é:", curtose)

desvio_padrao = df['salary_in_usd'].std()
print("O desvio padrão da coluna é:", desvio_padrao)


#não sei oq isso significa '-'

# Carregar dados do arquivo CSV usando pandas
dados = pd.read_csv('salaries.csv')

# Extrair ângulos e valores do DataFrame
angulos = dados['salary_in_usd'].values
valores = dados['experience_level'].values

# Criar um gráfico polar
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Converter ângulos para graus
angulos_graus = np.degrees(angulos)

# Plotar os pontos no gráfico polar
ax.plot(angulos, valores)

# Personalizar o gráfico
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
plt.title('Gráfico Polar')
plt.show()

# Carregar os dados do arquivo CSV
dados = pd.read_csv('salaries.csv')

# Preparar os dados
# Suponha que seu arquivo CSV tenha colunas 'Região' e 'Variável'
# Substitua 'Região' pelo nome da coluna que contém as informações geográficas e
# 'Variável' pelo nome da coluna que contém a variável a ser representada no cartograma
regioes = dados['salary_in_usd']
variavel = dados['experience_level']

# Redimensionar as regiões de acordo com a variável
# Aqui você pode aplicar diferentes técnicas de redimensionamento dependendo do tipo de cartograma que deseja criar

# Plotar o cartograma
plt.figure(figsize=(10, 6))
plt.bar(regioes, variavel)  # Este é um exemplo simples, você pode personalizar o tipo de gráfico de acordo com sua necessidade
plt.xlabel('salary_in_usd')
plt.ylabel('experience_level')
plt.title('Cartograma')
plt.xticks(rotation=45)  # Rotacionar os rótulos no eixo x para facilitar a leitura
plt.tight_layout()
plt.show()




# Carregar os dados do arquivo CSV
dados = pd.read_csv('salaries.csv')

# Extrair categorias e contagens do DataFrame
categorias = dados['experience_level']
contagens = dados['salary_in_usd']

# Plotar o pictograma
plt.figure(figsize=(8, 6))

# Loop através das categorias e plotar o número correspondente de símbolos
for i, categoria in enumerate(categorias):
    plt.scatter(i, 0, s=contagens[i]*100, label=categoria, alpha=0.5)  # Ajuste o tamanho do símbolo conforme a contagem

plt.xticks(range(len(categorias)), categorias)  # Rotular os eixos x com as categorias
plt.xlabel('Experiencia')
plt.ylabel('Salario')
plt.title('Pictograma')
plt.legend()
plt.tight_layout()
plt.show()

# ESTATÍSTICAS:
'''
media moda
mdeiana
curtose
desvio padrao
quartis
variancia
'''

# while True:
#     print("\n=== MENU ===")
#     print("1. Adicionar profissional")
#     print("2. Listar profissionais em ordem alfabetica")
#     print("3. Buscar profissional")
#     print("4. Remover profissional")
#     print("5. Remover relacionamento")
#     print("6. Salvar e sair")
#     opcao = input("Escolha uma opção: ")

#     if opcao == '1':
#         nome = input('Digite o nome do profissional: ')
#         if nome != '0':
#             profissionais[nome] = {}
#             profissionais[nome]['cargo'] = input('Digite o cargo: ')
#             profissionais[nome]['salario'] = input('Digite o salario: ')
#             profissionais[nome]['lista'] = []
#             while True:
#                 print('Digite o relacionamento, ou digite 0 para parar')
#                 resposta = input()
#                 if resposta == '0':
#                     break
#                 else:
#                     profissionais[nome]['lista'].append(resposta)
#         else:
#             break


#     elif opcao == '2':
#         # Imprime o dicionário ordenado
#         dicionario_ordenado = dict(sorted(profissionais.items()))
#         for chave, valor in dicionario_ordenado.items():
#             print(f'{chave}: {valor}')


#     elif opcao == '3':
#         nome = input('Digite o nome do profissional: ')
#         if nome in profissionais:
#             print(f'Nome: {nome}')
#             print(f'Cargo: {profissionais[nome]["cargo"]}')
#             print(f'Salário: {profissionais[nome]["salario"]}')
#             print(f'Relacionamentos:')
#             for relacionamento in profissionais[nome]['lista']:
#                 print(f'- {relacionamento}')
#         else:
#             print(f'O nome "{nome}" não foi encontrado no dicionário.')


#     elif opcao == '4':
#         remove = input("Digite o nome do profissional que deseja remover: ")
#         if remove in profissionais:
#             profissionais.pop(remove)
#             print(f"{remove} foi removido com sucesso!")
#         else:
#             print(f"{remove} não encontrado na lista de profissionais.")


#     elif opcao == '5':
#         profissional = input("Digite o nome do profissional que deseja alterar: ")
#         remove_relacionamento = input(f"Digite o nome do relacionamento de {profissional} que deseja remover: ")
#         if profissional in profissionais and remove_relacionamento in profissionais[profissional]['lista']:
#             profissionais[profissional]['lista'].remove(remove_relacionamento)
#             print(f"Relacionamento '{remove_relacionamento}' removido com sucesso para o profissional '{profissional}'.")
#         else:
#             print(f"O relacionamento '{remove_relacionamento}' não encontrado na lista de relacionamentos de '{profissional}'.")
    
    
#     elif opcao == '6':
#         #salvar em json
#         nome_arquivo = 'profissionais.json'
#         with open(nome_arquivo, 'w') as arquivo:
#             json.dump(profissionais, arquivo)

#         #salvar em .txt
#         nome_arquivo = 'profissionais.txt'
#         with open(nome_arquivo, 'w') as arquivo:
#             for chave, valor in profissionais.items():
#                 arquivo.write(f'{chave}: {valor}\n')
#         print("Dados salvos. Saindo do programa.")
#         break
    
    
#     else:
#         print("Opção inválida. Por favor, escolha uma opção válida.")
