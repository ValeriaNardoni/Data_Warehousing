import pandas as pd
import random


roi_df = pd.read_csv('roi.csv')
utenti_df = pd.read_csv('utenti.csv')
piattaforme_df = pd.read_csv('piattaforme.csv')
campagne_df = pd.read_csv('campagne.csv')
date_df = pd.read_csv('date.csv')

# Esegui le operazioni di JOIN
result_df = (
    roi_df
    .merge(utenti_df, left_on='id_utente', right_on='id_utente', how='inner')
    .merge(piattaforme_df, left_on='id_piattaforma', right_on='id_piattaforma', how='inner')
    .merge(campagne_df, left_on='id_campagna', right_on='id_campagna', how='inner')
    .merge(date_df, left_on='id_data', right_on='id_data', how='inner')
)


result_csv_file_path = 'risultato_query.csv'
result_df.to_csv(result_csv_file_path, index=False)

print(f"File CSV del risultato della query creato con successo: {result_csv_file_path}")

df = pd.read_csv('risultato_query.csv')

# Crea un dizionario di combinazioni e costi casuali
combinazioni_costi = {}
for index, row in df.iterrows():
    chiave_combinazione = (row['nome_y'], row['campagna'], row['tipologia'])
    if chiave_combinazione not in combinazioni_costi:
        combinazioni_costi[chiave_combinazione] = random.randint(80, 1000)


df['costo'] = df.apply(lambda row: combinazioni_costi[(row['nome_y'], row['campagna'], row['tipologia'])], axis=1)
result_csv_file_path = 'risultato_query.csv'
df.to_csv(result_csv_file_path, index=False)

print(f"File CSV del risultato con costi uniformi creato con successo: {result_csv_file_path}")
df = pd.read_csv('risultato_query.csv')
query = df[(df['ROI'] > 0) & ((df['mese'] == 12) | (df['mese'] == 11))]
risultato_finale = query[['ROI',"profitto", 'costo', 'campagna', 'tipologia']]

print(risultato_finale)