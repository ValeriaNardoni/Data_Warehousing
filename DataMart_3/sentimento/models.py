from django.db import models

class SentimentoMessaggi(models.Model):
    id_tipologia = models.IntegerField()
    id_piattaforma = models.IntegerField()
    id_utente = models.IntegerField()
    id_data = models.IntegerField()
    nuemero_messaggi = models.IntegerField()
    percentuale_sentimento = models.IntegerField()
    sentimento_medio = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.id_utente} - {self.timestamp}"
