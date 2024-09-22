# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Simulando dados de casos de saúde na comunidade
data = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out'],
    'Casos de Dengue': [100, 150, 200, 250, 300, 275, 225, 190, 170, 150],
    'Casos de Gripe': [80, 120, 160, 200, 240, 220, 180, 160, 140, 130]
}

# Criando DataFrame
df = pd.DataFrame(data)

# Visualizando os dados de casos de Dengue e Gripe ao longo do ano
plt.figure(figsize=(10, 6))
plt.plot(df['Mês'], df['Casos de Dengue'], marker='o', label='Dengue', color='b')
plt.plot(df['Mês'], df['Casos de Gripe'], marker='o', label='Gripe', color='r')

# Customizando o gráfico
plt.title('Casos de Dengue e Gripe na Comunidade - 2024')
plt.xlabel('Mês')
plt.ylabel('Número de Casos')
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
