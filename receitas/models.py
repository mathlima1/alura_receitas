from django.db import models
from datetime import datetime

# Create your models here.
class Receita(models.Model):
    nome_da_receita = models.CharField(max_length = 200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length = 200)
    categorias = models.TextField()
    data_reecita = models.DateTimeField(default = datetime.now, blank = True)