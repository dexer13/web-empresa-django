from django.db import models
from ckeditor.fields import RichTextField
class Pages(models.Model):
    key=models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    title=models.CharField(verbose_name="titulo", max_length=200)
    content=RichTextField(verbose_name='contenido')
    order=models.SmallIntegerField(verbose_name='orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order','-title']
# Create your models here.
