import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

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

# =======     MÉDIA    =======
media = df['salary_in_usd'].mean()
print("A média de salário em dólares é: ")

# =======     MODA     =======
moda = df['salary_in_usd'].mode().values[0]
print("A moda de salário em dólares é: ", moda)

# =======    MEDIANA   =======
mediana = df['salary_in_usd'].median()
print("A mediana de salário em dólares é: ", mediana)

# =======     VARIÂNCIA     =======
variancia = df['salary_in_usd'].var()
print("A variância de salário em dólares é: ", variancia)

# =======     QUARTIS     =======
quartis = df['salary_in_usd'].quantile([0.25, 0.5, 0.75]).values
print("Os quartis de salário em dólares são: ", quartis)

# =======     CURTOSE     =======
curtose = df['salary_in_usd'].kurtosis()
print("A curtose de salário em dólares é: ", curtose)

# =======  DESVIO PADRÃO  =======
desvio_padrao = df['salary_in_usd'].std()
print("O desvio padrão de salário em dólares é: ", desvio_padrao)

# =======  AMPLITUDE TOTAL  =======
amplitude_total = df['salary_in_usd'].max() - df['salary_in_usd'].min()
print("A amplitude total de salário em dólares é: ", amplitude_total)

# =======    ASSIMETRIA    =======
assimetria = df['salary_in_usd'].skew()
print("A assimetria de salário em dólares é: ", assimetria)

# =======   CORRELAÇÃO LINEAR   =======
correlacao_linear = df['salary_in_usd'].corr(df['work_year'])
print('A correlação linear entre salário em dólares e ano trabalhado:', correlacao_linear)
# a.   se r = +1, há uma correlação perfeita e positiva entre as variáveis;
# b.   se r = –1, há uma correlação perfeita e negativa entre as variáveis;
# c.   se r = 0, ou não há correlação entre as variáveis, ou a relação que porventura exista não é linear.

# =======   REGRESSÃO   =======
# Definindo a constante de X
df['constante'] = 1
# Defina as variáveis independentes (X) e dependentes (y)
X = df[['constante', 'work_year']]
y = df['salary_in_usd']

# Ajuste o modelo de regressão linear
modelo = sm.OLS(y, X).fit()

# Imprima os resultados da regressão
print(modelo.summary())

# Extrapolando para um novo valor de work_year (2025)
novo_work_year_extrap = 2025  # Valor fora do intervalo original dos dados
novo_X_extrap = [1, novo_work_year_extrap]  # Novo ponto para extrapolação
salario_extrap = modelo.predict(novo_X_extrap)[0]
print(f"Salário estimado para work_year={novo_work_year_extrap}: ${salario_extrap:.2f}")

# Interpolando para um novo valor de work_year (2022.5)
novo_work_year_interp = 2022.5  # Valor dentro do intervalo original dos dados
novo_X_interp = [1, novo_work_year_interp]  # Novo ponto para interpolação
salario_interp = modelo.predict(novo_X_interp)[0]
print(f"Salário estimado para work_year={novo_work_year_interp}: ${salario_interp:.2f}")
# ============================

# =======     DISPERSÃO     =======
# Crie o diagrama de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['work_year'], df['salary_in_usd'], alpha=0.5)
plt.title('Diagrama de Dispersão: Salário x Ano Trabalhado')
plt.xlabel('Ano Trabalhado')
plt.ylabel('Salário')
plt.grid(True)
plt.show()
# =============================
