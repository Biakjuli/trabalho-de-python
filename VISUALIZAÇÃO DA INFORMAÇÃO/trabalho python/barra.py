import matplotlib.pyplot as plt

# Dados para plotagem
paises = ['Brasil', 'Espanha', 'França', 'México', 'Reino Unido']
percentuais_whatsapp = [98, 93, 95, 69, 57]
percentuais_telegram = [51, 37, 36, 10, 8]

# Configuração do gráfico de barras
fig, ax = plt.subplots()
largura_barra = 0.35
indice = range(len(paises))

barra1 = ax.bar(indice, percentuais_whatsapp, largura_barra,
                label='WhatsApp', color='orange')

barra2 = ax.bar([i + largura_barra for i in indice], percentuais_telegram,
                largura_barra, label='Telegram', color='blue')

# Adicionando rótulos e título
ax.set_xlabel('País')
ax.set_ylabel('Percentual')
ax.set_title('Uso do WhatsApp e Telegram por País')
ax.set_xticks([i + largura_barra / 2 for i in indice])
ax.set_xticklabels(paises)
ax.legend()

# Exibindo o gráfico
plt.show()