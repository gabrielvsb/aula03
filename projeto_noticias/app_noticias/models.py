from django.db import models

# Create your models here.
class Noticia(models.Model):
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
    titulo = models.CharField('titulo', max_length=128)
    conteudo = models.TextField()
