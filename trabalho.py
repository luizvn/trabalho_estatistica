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

amplitude_total = df['salary_in_usd'].max() - df['salary_in_usd'].min()
print("A amplitude total é:", amplitude_total)

assimetria = df['salary_in_usd'].skew()
print("A assimetria é: ", assimetria)

correlacao_linear = df['salary_in_usd'].corr(df['work_year'])
print('A correlação linear entre salário em dólares e ano trabalhado:', correlacao_linear)
# a.   se r = +1, há uma correlação perfeita e positiva entre as variáveis;
# b.   se r = –1, há uma correlação perfeita e negativa entre as variáveis;
# c.   se r = 0, ou não há correlação entre as variáveis, ou a relação que porventura exista não é linear.
# ============================
# Crie o diagrama de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['work_year'], df['salary_in_usd'], alpha=0.5)
plt.title('Diagrama de Dispersão: Salário x Ano Trabalhado')
plt.xlabel('Ano Trabalhado')
plt.ylabel('Salário')
plt.grid(True)
plt.show()


# =============================



# ==========================


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

