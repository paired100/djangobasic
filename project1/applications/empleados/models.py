from django.db import models
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidades trabajor'
        verbose_name_plural = 'Habilidad Tecnica'
        ordering = ['id']
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
class Persona(models.Model):
    jobs = (
        ('0','SRE'),
        ('1','Economista'),
        ('2','Developer'),
        ('3','Test Automation')
    )
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=1,choices=jobs)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    def __str__(self):
        return str(self.id) + '-'+ self.first_name + '-' + self.last_name
    
    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Datos de trabajador'
        ordering = ['id']