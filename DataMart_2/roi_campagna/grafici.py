import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 



df = pd.read_csv('risultato_query.csv')

# Raggruppa i dati per campagna e calcola la media del ROI
agg_data = df.groupby('campagna').agg({
    'ROI': 'mean'
}).reset_index()

# Creazione del grafico
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.4
index = range(len(agg_data))

bars = ax.bar(index, agg_data.ROI, bar_width, label='Media ROI', color='pink')

ax.set_xlabel('Campagne')
ax.set_ylabel('Media ROI %')
ax.set_title('Media del ROI al variare della campagna')
ax.set_xticks([i for i in index])
ax.set_xticklabels(agg_data.campagna)
ax.legend()

plt.show()



result_df = pd.read_csv('risultato_query.csv')

bins = [18, 28, 39, 50, 61, 72, 83]
labels = ['18-28', '29-39', '40-50', '51-61', '62-72', '73-83']
result_df['fascia_eta'] = pd.cut(result_df['età'], bins=bins, labels=labels, right=False)

# Calcola la media del ROI per ogni fascia d'età e campagna
media_roi_per_fascia_eta_campagna = result_df.groupby(['fascia_eta', 'campagna'])['ROI'].mean().reset_index()


sns.set(style="whitegrid")
unique_campaigns = media_roi_per_fascia_eta_campagna['campagna'].unique()
x_positions = np.arange(len(labels))
bar_width = 0.15

fig, ax = plt.subplots(figsize=(14, 8))

for i, campaign in enumerate(unique_campaigns):
    campaign_data = media_roi_per_fascia_eta_campagna[media_roi_per_fascia_eta_campagna['campagna'] == campaign]
    bar_positions = x_positions - (len(unique_campaigns) / 2) * bar_width + i * bar_width
    ax.bar(bar_positions, campaign_data['ROI'], bar_width,
           align='center',
           linewidth=1, edgecolor='k',
           alpha=0.7,
           label=f'Campagna {campaign}')


ax.set_xticks(x_positions)
ax.set_xticklabels(labels)
ax.legend()
ax.set_xlabel('Fascia d\'Età')
ax.set_ylabel('Media ROI %')
ax.set_title('Media del ROI al variare delle Campagne e delle Fasce d\'Età')

plt.show()