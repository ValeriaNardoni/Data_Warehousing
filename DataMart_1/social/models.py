from django.db import models

class InterazioniSocial(models.Model):
    id_utente = models.IntegerField()
    id_piattaforma = models.IntegerField()
    id_contenuti = models.IntegerField()
    id_data = models.IntegerField()
    commenti = models.IntegerField()
    like = models.IntegerField()
    condivisioni = models.IntegerField()
    click = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.id_utente} - {self.timestamp}"
