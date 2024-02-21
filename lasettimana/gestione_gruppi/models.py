from django.db import models

class Gruppo(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=20)
    data_arrivo = models.DateField()
    data_partenza = models.DateField()
    
    def __str__(self):
       return self.nome + ' ' + self.cognome

    class Meta:
        verbose_name = 'Gruppo'
        verbose_name_plural = 'Gruppi'
 

class MembroGruppo(models.Model):
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=20)
    data_arrivo = models.DateField()
    data_partenza = models.DateField()

    def __str__(self):
        return self.nome + ' ' +self.cognome
    
    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membri'