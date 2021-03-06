# Generated by Django 2.1.3 on 2018-11-07 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('telefono', models.IntegerField(max_length=8)),
                ('fecha_nacimiento', models.DateField()),
                ('DPI', models.IntegerField(max_length=13)),
                ('experiencia', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bolsadetrabajo.Solicitante')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('requisitos', models.CharField(max_length=700)),
                ('conocimientos', models.CharField(max_length=700)),
                ('beneficios', models.CharField(max_length=700)),
                ('solicitantes', models.ManyToManyField(through='bolsadetrabajo.Solicitud', to='bolsadetrabajo.Solicitante')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bolsadetrabajo.Trabajo'),
        ),
    ]
