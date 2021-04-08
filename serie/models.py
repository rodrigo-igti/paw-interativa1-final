from django.db import models


class Serie(models.Model):
    nome = models.CharField("Título da Série", max_length=150)
    idGenero = models.ForeignKey('genero.Genero', verbose_name="Gênero", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

