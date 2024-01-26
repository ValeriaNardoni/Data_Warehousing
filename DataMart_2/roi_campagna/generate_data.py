import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Genera dati casuali per gli utenti
users_data = []
for user_id in range(1, 1001):
    users_data.append({
        "id_utente": user_id,
        "nome": fake.first_name(),
        "cognome": fake.last_name(),
        "email": fake.email(),
        "contatto": fake.phone_number(),
        "demografia": fake.city(),
        "età": random.randint(18, 80), 
    })


users_csv_file_path = 'utenti.csv'
users_fieldnames = ["id_utente", "nome", "cognome", "email", "contatto", "demografia", "età"]

with open(users_csv_file_path, 'w', newline='') as users_csv_file:
    users_csv_writer = csv.DictWriter(users_csv_file, fieldnames=users_fieldnames)
    users_csv_writer.writeheader()

    for user_data in users_data:
        users_csv_writer.writerow(user_data)

print(f"File CSV degli utenti creato con successo: {users_csv_file_path}")

# Genera dati casuali per le piattaforme sociali
piattaforme_data = []
social_media_names = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'Pinterest', 'Reddit', 'TikTok', 'YouTube']

for piattaforma_id, name in enumerate(social_media_names):
    piattaforme_data.append({
        "id_piattaforma": piattaforma_id,
        "nome": name,
    })


piattaforme_csv_file_path = 'piattaforme.csv'
piattaforme_fieldnames = ["id_piattaforma", "nome"]

with open(piattaforme_csv_file_path, 'w', newline='') as piattaforme_csv_file:
    piattaforme_csv_writer = csv.DictWriter(piattaforme_csv_file, fieldnames=piattaforme_fieldnames)
    piattaforme_csv_writer.writeheader()

    for piattaforma_data in piattaforme_data:
        piattaforme_csv_writer.writerow(piattaforma_data)

print(f"File CSV delle piattaforme creato con successo: {piattaforme_csv_file_path}")


tipologie_possibili = ['Immagine', 'Testo', 'Video', 'Canzone']
campagne_possibili = ['Lancio Prodotto', 'Acquisizione Clienti', 'Event Marketing', 'Influencer Marketing', 'Retargeting']

# Genera dati casuali per i contenuti sociali
contenuti_sociali_data = []
combinazioni_possibili = []

for campagna_id in range(1, 101):
    id_campagna = campagna_id
    tipologia_contenuto = random.choice(tipologie_possibili)
    campagne_contenuto = random.choice(campagne_possibili)

    combinazione = f"{id_campagna}_{tipologia_contenuto}"
    while combinazione in combinazioni_possibili:
        tipologia_contenuto = random.choice(tipologie_possibili)
        combinazione = f"{id_campagna}_{tipologia_contenuto}"

    combinazioni_possibili.append(combinazione)

    contenuti_sociali_data.append({
        "id_campagna": id_campagna,
        "campagna": campagne_contenuto,
        "tipologia": tipologia_contenuto,
    })


contenuti_sociali_csv_file_path = 'campagne.csv'
contenuti_sociali_fieldnames = ["id_campagna",  "campagna", "tipologia"]

with open(contenuti_sociali_csv_file_path, 'w', newline='') as contenuti_sociali_csv_file:
    contenuti_sociali_csv_writer = csv.DictWriter(contenuti_sociali_csv_file, fieldnames=contenuti_sociali_fieldnames)
    contenuti_sociali_csv_writer.writeheader()

    for contenuto_sociali_data in contenuti_sociali_data:
        contenuti_sociali_csv_writer.writerow(contenuto_sociali_data)

print(f"File CSV dei contenuti sociali creato con successo: {contenuti_sociali_csv_file_path}")

date_data = []
for date_id in range(1, 366):
    date = (datetime.now() - timedelta(days=date_id))
    date_data.append({
        "id_data": date_id,
        "anno": date.year,
        "mese": date.month,
    })


date_csv_file_path = 'date.csv'
date_fieldnames = ["id_data", "anno", "mese"]

with open(date_csv_file_path, 'w', newline='') as date_csv_file:
    date_csv_writer = csv.DictWriter(date_csv_file, fieldnames=date_fieldnames)
    date_csv_writer.writeheader()

    for date_data_item in date_data:
        date_csv_writer.writerow(date_data_item)

print(f"File CSV delle date creato con successo: {date_csv_file_path}")

costi_per_combinazione = {}

# Genera dati casuali 
roi_data = []
for _ in range(100):
    user_id = random.choice(users_data)["id_utente"]
    piattaforma_data = random.choice(piattaforme_data)
    piattaforma_id = piattaforma_data["id_piattaforma"]
    campagna_data = random.choice(contenuti_sociali_data)
    campagna_id = campagna_data["id_campagna"]
    tipologia = campagna_data["tipologia"]
    data_id = random.choice(date_data)["id_data"]

    # Genera un costo o riutilizza il costo se la combinazione è già presente nel dizionario
    combinazione = f"{campagna_id}_{tipologia}_{piattaforma_id}"
    if combinazione not in costi_per_combinazione:
        costo_campagna = random.randint(80, 1000)
        costi_per_combinazione[combinazione] = costo_campagna
    else:
        costo_campagna = costi_per_combinazione[combinazione]

    profitto = random.randint(50, 1000)
    roi_100 = ((profitto - costo_campagna) / costo_campagna) * 100

    roi_data.append({
        "model": "roi_campagna.marketing",
        "pk": None,
        "fields": {
            "id_utente": user_id,
            "id_piattaforma": piattaforma_id,
            "id_campagna": campagna_id,
            "id_data": data_id,
            "costo": costo_campagna,
            "profitto": profitto,
            "ROI": roi_100,
            "timestamp": fake.date_time_between(start_date="-1y", end_date="now").strftime('%Y-%m-%dT%H:%M:%SZ'),
        }
    })

roi_csv_file_path = 'roi.csv'
roi_fieldnames = ["id_utente", "id_piattaforma", "id_campagna", "id_data", "costo", "profitto", "ROI", "timestamp"]

with open(roi_csv_file_path, 'w', newline='') as roi_csv_file:
    interazioni_social_csv_writer = csv.DictWriter(roi_csv_file, fieldnames=roi_fieldnames)
    interazioni_social_csv_writer.writeheader()

    for interazione_social_data in roi_data:
        interazioni_social_csv_writer.writerow(interazione_social_data["fields"])

print(f"File CSV delle interazioni sociali creato con successo: {roi_csv_file_path}")