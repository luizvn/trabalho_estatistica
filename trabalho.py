import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ======= LENDO O ARQUIVO =======
dados = pd.read_csv("salaries.csv")

df = pd.DataFrame(dados)

# ======= MÉDIA DOS SALÁRIOS PARA TRABALHO =======
job_title_media = dados.groupby("job_title")["salary_in_usd"].mean()

# ======= PLOT DO GRÁFICO 'TRABALHO X SALARIO(USD)' =======

barra_salarie_per_jobtitle = plt.figure("grafico_de_barras_salarie_per_jobtitle")

job_title_media.plot.bar()

plt.show()

# ======= MÉDIA DOS SALÁRIOS PARA NÍVEL DE EXPERIÊNCIA =======
experience_level_media = dados.groupby("experience_level")["salary_in_usd"].mean()

# ======= PLOT DO GRÁFICO 'EXPERIÊNCIA X SALÁRIAO(USD)' =======
barra_salarie_per_experience_level = plt.figure("grafico_de_barras_salarie_per_experience_level")

experience_level_media.plot.bar()

plt.show()

# ======= ESTATÍSTICAS =======
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
# ============================

# ======= GRÁFICO POLAR =======
# Extrair ângulos e valores do DataFrame:
angulos = dados['salary_in_usd'].values
valores = dados['experience_level'].values

# Criar um gráfico polar:
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
# =============================

# ======= CARTOGRAMA =======
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

# ==========================

# ======= PICTOGRAMA =======
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
# ==========================

# ESTATÍSTICAS:
'''
media moda
mdeiana
curtose
desvio padrao
quartis
variancia
'''

