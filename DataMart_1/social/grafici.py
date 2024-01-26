import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


result_df = pd.read_csv('risultato_query.csv')

bins = [18, 28, 39, 50, 61, 72, 83]
labels = ['18-28', '29-39', '40-50', '51-61', '62-72', '73-83']
result_df['fascia_eta'] = pd.cut(result_df['età'], bins=bins, labels=labels, right=False)

# Calcola la media dei like, commenti, ecc. per ogni fascia d'età
media_per_fascia_eta = result_df.groupby('fascia_eta').agg({
    'like': 'mean',
    'commenti': 'mean',
    'condivisioni': 'mean',
    'click': 'mean',

}).reset_index()

print(media_per_fascia_eta)
sns.set(style="whitegrid")

x_positions = np.arange(len(media_per_fascia_eta['fascia_eta']))
number_of_groups = len(media_per_fascia_eta.columns) - 1  # Escludi la colonna 'fascia_eta'
fill_factor = 0.8  # rapporto della larghezza dei gruppi
bar_width = np.diff(x_positions).min() / number_of_groups * fill_factor


colors = sns.color_palette("pastel", len(result_df.columns) - 1)
labels = media_per_fascia_eta.columns[1:]  # Escludi la colonna 'fascia_eta'

# Crea il grafico a barre
for i, column in enumerate(labels):
    bar_positions = x_positions - number_of_groups * bar_width / 2 + (i + 0.5) * bar_width
    plt.bar(bar_positions, media_per_fascia_eta[column], bar_width,
            align='center',
            linewidth=1, edgecolor='k',
            color=colors[i], alpha=0.7,
            label=column.capitalize())

# Imposta le etichette e la legenda
plt.xticks(x_positions, labels=media_per_fascia_eta['fascia_eta'])
plt.legend()
plt.xlabel('Fascia d\'Età')
plt.ylabel('Media')
plt.title('Media di Like, Commenti, Condivisioni e Click per Fascia d\'Età')


plt.show()

df = pd.read_csv('risultato_query.csv')
# Raggruppa i dati per categoria e calcola la somma di like, commenti, condivisioni e click
agg_data = df.groupby('tipologia').agg({
    'commenti': 'sum',
    'like': 'sum',
    'condivisioni': 'sum',
    'click': 'sum'
}).reset_index()

print(agg_data)



fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(len(agg_data))

bar1 = ax.bar(index, agg_data.like, bar_width, label='Like')
bar2 = ax.bar([i + bar_width for i in index], agg_data.condivisioni, bar_width, label='Condivisioni')
bar3 = ax.bar([i + 2 * bar_width for i in index], agg_data.click, bar_width, label='Click')
bar3 = ax.bar([i + 3 * bar_width for i in index], agg_data.commenti, bar_width, label='Commenti')

ax.set_xlabel('Tipologie')
ax.set_ylabel('Quantità')
ax.set_title('Statistiche Tipologie')
ax.set_xticks([i + bar_width for i in index])
ax.set_xticklabels(agg_data.tipologia)
ax.legend()

plt.show()

df_december = df.query('mese == 12 or mese == 11')

# Raggruppa i dati per categoria e calcola la somma di like, commenti, condivisioni e click
agg_data = df_december.groupby('categoria').agg({
    'commenti': 'sum',
    'like': 'sum',
    'condivisioni': 'sum',
    'click': 'sum'
}).reset_index()


fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(len(agg_data))

bar1 = ax.bar(index, agg_data.like, bar_width, label='Like')
bar2 = ax.bar([i + bar_width for i in index], agg_data.condivisioni, bar_width, label='Condivisioni')
bar3 = ax.bar([i + 2 * bar_width for i in index], agg_data.click, bar_width, label='Click')
bar3 = ax.bar([i + 3 * bar_width for i in index], agg_data.commenti, bar_width, label='Commenti')

ax.set_xlabel('Categorie')
ax.set_ylabel('Quantità')
ax.set_title('Statistiche delle storie per categoria (Mese 12 e Mese 11)')
ax.set_xticks([i + bar_width for i in index])
ax.set_xticklabels(agg_data.categoria)
ax.legend()

plt.show()