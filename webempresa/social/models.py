from django.db import models


class Link(models.Model):
    key=models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name=models.CharField(verbose_name="Red Social", max_length=200)
    url=models.URLField(verbose_name='enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['-name']