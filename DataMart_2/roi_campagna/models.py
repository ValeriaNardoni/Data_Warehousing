from django.db import models

class Marketing(models.Model):
    id_campagna = models.IntegerField()
    id_piattaforma = models.IntegerField()
    id_utente = models.IntegerField()
    id_data = models.IntegerField()
    costo = models.IntegerField()
    profitto = models.IntegerField()
    roi = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.id_utente} - {self.timestamp}"
