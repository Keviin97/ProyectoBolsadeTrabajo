# Generated by Django 2.1.3 on 2018-11-07 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bolsadetrabajo', '0002_auto_20181107_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]