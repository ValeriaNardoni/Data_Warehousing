import pandas as pd
from pandasql import sqldf


sentimento_df = pd.read_csv('sentimento.csv')
utenti_df = pd.read_csv('utenti.csv')
piattaforme_df = pd.read_csv('piattaforme.csv')
tipologie_df = pd.read_csv('tipologia.csv')
date_df = pd.read_csv('date.csv')

# Esegui le operazioni di JOIN
result_df = (
    sentimento_df
    .merge(utenti_df, left_on='id_utente', right_on='id_utente', how='inner')
    .merge(piattaforme_df, left_on='id_piattaforma', right_on='id_piattaforma', how='inner')
    .merge(tipologie_df, left_on='id_tipologia', right_on='id_tipologia', how='inner')
    .merge(date_df, left_on='id_data', right_on='id_data', how='inner')
)


result_csv_file_path = 'risultato_query.csv'
result_df.to_csv(result_csv_file_path, index=False)

print(f"File CSV del risultato della query creato con successo: {result_csv_file_path}")

df = pd.read_csv('risultato_query.csv')

utenti_positivi_youtube = df[(df['tipologiaSentimento'] == 'Positivo') & (df['nome_y'] == 'YouTube')]
risultato_finale = utenti_positivi_youtube[['id_utente', 'età', 'nome_x', 'cognome', 'demografia']]

print(risultato_finale)