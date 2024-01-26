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

# Genera dati casuali 
tipologie_data = []
sentiment_names = ['Positivo', 'Neutro', 'Negativo']

for tipologia_id, name in enumerate(sentiment_names):
    tipologie_data.append({
        "id_tipologia": tipologia_id,
        "tipologiaSentimento": name,
    })


tipologie_csv_file_path = 'tipologia.csv'
tipologie_fieldnames = ["id_tipologia", "tipologiaSentimento"]

with open(tipologie_csv_file_path, 'w', newline='') as tipologie_csv_file:
    tipologie_csv_writer = csv.DictWriter(tipologie_csv_file, fieldnames=tipologie_fieldnames)
    tipologie_csv_writer.writeheader()

    for tipologia_data in tipologie_data:
        tipologie_csv_writer.writerow(tipologia_data)

print(f"File CSV delle tipologie creato con successo: {tipologie_csv_file_path}")

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


roi_data = []
for _ in range(100):
    user_id = random.choice(users_data)["id_utente"]
    piattaforma_id = random.choice(piattaforme_data)["id_piattaforma"]
    tipologia_sentimento = random.choice(tipologie_data)
    data_id = random.choice(date_data)["id_data"]

    numero = random.randint(0, 1000)

    # Utilizza la tipologia di sentimento reale per calcolare le metriche
    if tipologia_sentimento["tipologiaSentimento"] == 'Positivo':
        percentuale_sentimento = random.uniform(70, 100)
        sentimento_medio = random.uniform(0.5, 1)
    elif tipologia_sentimento["tipologiaSentimento"] == 'Negativo':
        percentuale_sentimento = random.uniform(0, 30)
        sentimento_medio = random.uniform(-1, -0.5)
    else:  # 'Neutro'
        percentuale_sentimento = random.uniform(30, 70)
        sentimento_medio = random.uniform(-0.5, 0.5)


    roi_data.append({
        "model": "sentimento.sentimentomessaggi",
        "pk": None,
        "fields": {
            "id_utente": user_id,
            "id_piattaforma": piattaforma_id,
            "id_tipologia": tipologia_sentimento["id_tipologia"],
            "id_data": data_id,
            "numero_messaggi": numero,
            "percentuale_sentimento": percentuale_sentimento,
            "sentimento_medio": sentimento_medio,
            "timestamp": fake.date_time_between(start_date="-1y", end_date="now").strftime('%Y-%m-%dT%H:%M:%SZ'),
        }
    })


roi_csv_file_path = 'sentimento.csv'
roi_fieldnames = ["id_utente", "id_piattaforma", "id_tipologia", "id_data", "numero_messaggi",  "percentuale_sentimento", "sentimento_medio", "timestamp"]

with open(roi_csv_file_path, 'w', newline='') as roi_csv_file:
    interazioni_social_csv_writer = csv.DictWriter(roi_csv_file, fieldnames=roi_fieldnames)
    interazioni_social_csv_writer.writeheader()

    for interazione_social_data in roi_data:
        interazioni_social_csv_writer.writerow(interazione_social_data["fields"])

print(f"File CSV delle interazioni sociali creato con successo: {roi_csv_file_path}")