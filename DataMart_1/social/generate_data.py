import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


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
categorie_possibili = ['Storia d\'amore', 'Storia divertente', 'Storia avventurosa', 'Storia drammatica', 'Storia fantasy']


contenuti_sociali_data = []
combinazioni_possibili = []

for contenuto_id in range(1, 101):
    id_contenuto = contenuto_id
    tipologia_contenuto = random.choice(tipologie_possibili)
    categoria_contenuto = random.choice(categorie_possibili)

    combinazione = f"{id_contenuto}_{tipologia_contenuto}"
    while combinazione in combinazioni_possibili:
        tipologia_contenuto = random.choice(tipologie_possibili)
        combinazione = f"{id_contenuto}_{tipologia_contenuto}"

    combinazioni_possibili.append(combinazione)

    contenuti_sociali_data.append({
        "id_contenuto": id_contenuto,
        "categoria": categoria_contenuto,
        "tipologia": tipologia_contenuto,
    })


contenuti_sociali_csv_file_path = 'contenuti_sociali.csv'
contenuti_sociali_fieldnames = ["id_contenuto",  "categoria", "tipologia"]

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

# Genera dati casuali per le interazioni sociali
interazioni_social_data = []
for _ in range(100):
    user_id = random.choice(users_data)["id_utente"]
    piattaforma_id = random.choice(piattaforme_data)["id_piattaforma"]
    contenuto_id = random.choice(contenuti_sociali_data)["id_contenuto"]
    data_id = random.choice(date_data)["id_data"]

    interazioni_social_data.append({
        "model": "social.interazionisocial",
        "pk": None,
        "fields": {
            "id_utente": user_id,
            "id_piattaforma": piattaforma_id,
            "id_contenuti": contenuto_id,
            "id_data": data_id,
            "commenti": random.randint(0, 100),
            "like": random.randint(0, 1000),
            "condivisioni": random.randint(0, 500),
            "click": random.randint(0, 200),
            "timestamp": fake.date_time_between(start_date="-1y", end_date="now").strftime('%Y-%m-%dT%H:%M:%SZ'),
        }
    })


interazioni_social_csv_file_path = 'interazioni_social.csv'
interazioni_social_fieldnames = ["id_utente", "id_piattaforma", "id_contenuti", "id_data", "commenti", "like", "condivisioni", "click", "timestamp"]

with open(interazioni_social_csv_file_path, 'w', newline='') as interazioni_social_csv_file:
    interazioni_social_csv_writer = csv.DictWriter(interazioni_social_csv_file, fieldnames=interazioni_social_fieldnames)
    interazioni_social_csv_writer.writeheader()

    for interazione_social_data in interazioni_social_data:
        interazioni_social_csv_writer.writerow(interazione_social_data["fields"])

print(f"File CSV delle interazioni sociali creato con successo: {interazioni_social_csv_file_path}")