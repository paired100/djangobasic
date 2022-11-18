# Generated by Django 4.1.3 on 2022-11-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidades trabajor',
                'verbose_name_plural': 'Habilidad Tecnica',
            },
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['first_name'], 'verbose_name': 'Trabajador', 'verbose_name_plural': 'Datos de trabajador'},
        ),
        migrations.AddField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]