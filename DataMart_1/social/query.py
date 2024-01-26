import pandas as pd

# Carica i dati dai file CSV in DataFrame
interazioni_social_df = pd.read_csv('interazioni_social.csv')
utenti_df = pd.read_csv('utenti.csv')
piattaforme_df = pd.read_csv('piattaforme.csv')
contenuti_sociali_df = pd.read_csv('contenuti_sociali.csv')
date_df = pd.read_csv('date.csv')

# Esegui le operazioni di JOIN
result_df = (
    interazioni_social_df
    .merge(utenti_df, left_on='id_utente', right_on='id_utente', how='inner')
    .merge(piattaforme_df, left_on='id_piattaforma', right_on='id_piattaforma', how='inner')
    .merge(contenuti_sociali_df, left_on='id_contenuti', right_on='id_contenuto', how='inner')
    .merge(date_df, left_on='id_data', right_on='id_data', how='inner')
)

# Salva i risultati in un nuovo file CSV
result_csv_file_path = 'risultato_query.csv'
result_df.to_csv(result_csv_file_path, index=False)

print(f"File CSV del risultato della query creato con successo: {result_csv_file_path}")


df = pd.read_csv('risultato_query.csv')

query = df[(df['click'] < 20)]
risultato_finale = query[['categoria', 'tipologia', 'nome_x', 'cognome', 'età']]

print(risultato_finale)

