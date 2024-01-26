
import json
from django.shortcuts import render
from .models import InterazioniSocial
from datetime import datetime

def populate_data():
    with open('interazioni_social.json', 'r') as json_file:
        data = json.load(json_file)

    for entry in data:
        interazione_social = InterazioniSocial(
            id_utente=entry['fields']['id_utente'],
            id_piattaforma=entry['fields']['id_piattaforma'],
            id_contenuti=entry['fields']['id_contenuti'],
            id_data=entry['fields']['id_data'],
            commenti=entry['fields']['commenti'],
            like=entry['fields']['like'],
            condivisioni=entry['fields']['condivisioni'],
            click=entry['fields']['click'],
            timestamp=datetime.strptime(entry['fields']['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        )
        interazione_social.save()

    print("Dati caricati con successo nel database.")

# Chiamata alla funzione di popolamento solo se lo script viene eseguito direttamente
if __name__ == "__main__":
    populate_data()
