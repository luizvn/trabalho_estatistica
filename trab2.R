# Instalar e carregar os pacotes necessários
install.packages("dplyr")
install.packages("BSDA")
library(dplyr)
library(BSDA)

# Ler o arquivo CSV
data <- read.csv("salaries.csv")

# Verificar a estrutura dos dados
# str(data)

# Verificar os primeiros valores da coluna 'salaries_in_usd'
head(data$salary_in_usd)

# Verificar se há valores não numéricos na coluna 'salaries_in_usd'
non_numeric_values <- data$salary_in_usd[!grepl("^\\d+$", data$salary_in_usd)]
# print(non_numeric_values)

# Converter a coluna 'salaries_in_usd' para numérica
data$salary_in_usd <- as.numeric(as.character(data$salary_in_usd))

# Filtrar os dados para incluir apenas as e 'experience_level' é 'SE'
data_us_se <- data %>%
  filter(experience_level == "SE")

# Calcular a média populacional conhecida (média geral de 'salaries_in_usd')
pop_mean <- mean(data$salary_in_usd, na.rm = TRUE)

# Calcular o desvio padrão populacional conhecido (desvio padrão geral de 'salaries_in_usd')
pop_sd <- sd(data$salary_in_usd, na.rm = TRUE)
print(paste("Desvio padrão: ", pop_sd))

# Calcular a média e outras estatísticas descritivas necessárias para a amostra filtrada
sample_mean <- mean(data_us_se$salary_in_usd, na.rm = TRUE)
sample_size <- sum(!is.na(data_us_se$salary_in_usd))

# Verificar a média populacional e a amostral
print(paste("Média populacional:", pop_mean))
print(paste("Média da amostra:", sample_mean))

# Realizar o teste Z
z_result <- z.test(x = data_us_se$salary_in_usd, mu = pop_mean, sigma.x = pop_sd, alternative = "two.sided")

# Exibir o resultado do teste Z
print(z_result)
