from django.contrib import admin

from .models import Persona,Habilidades

# Register your models here.


admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento'
    )
    search_fields = ('first_name',)
    list_filter = ('job','habilidades')
    
    filter_horizontal = ('habilidades',)
admin.site.register(Persona,EmpleadoAdmin)