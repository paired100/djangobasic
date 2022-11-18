from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=100,)
    short_name = models.CharField('Nombre Corto', max_length=30)
    anulate = models.BooleanField('Anulado',default=False)
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name
    class Meta:
        verbose_name = 'Departamentos Nomina'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['id']
        unique_together = ('name','short_name')
        