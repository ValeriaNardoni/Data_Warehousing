import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


result_df = pd.read_csv('risultato_query.csv')
conteggio_messaggi_per_piattaforma_sentimento = result_df.groupby(['nome_y', 'tipologiaSentimento']).size().unstack(fill_value=0)
sns.set(style="whitegrid")


fig, ax = plt.subplots(figsize=(14, 8))
colors = sns.color_palette('pastel', n_colors=len(conteggio_messaggi_per_piattaforma_sentimento.columns))

# Creazione delle barre raggruppate per ogni piattaforma
bar_width = 0.2
bar_positions = np.arange(len(conteggio_messaggi_per_piattaforma_sentimento))

for i, sentiment_type in enumerate(conteggio_messaggi_per_piattaforma_sentimento.columns):
    ax.bar(bar_positions + i * bar_width, conteggio_messaggi_per_piattaforma_sentimento[sentiment_type], bar_width,
           label=sentiment_type, color=colors[i])


ax.set_xticks(bar_positions + (len(conteggio_messaggi_per_piattaforma_sentimento.columns) - 1) * bar_width / 2)
ax.set_xticklabels(conteggio_messaggi_per_piattaforma_sentimento.index)
ax.legend(title='Tipologia di Sentimento')
ax.set_xlabel('Piattaforma')
ax.set_ylabel('Numero di Messaggi')
ax.set_title('Numero di Messaggi per Tipologia di Sentimento e Piattaforma')


plt.show()
result_df = pd.read_csv('risultato_query.csv')

