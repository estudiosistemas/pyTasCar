# Generated by Django 2.2.6 on 2019-10-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('Permiso', models.CharField(choices=[('T', 'Control Total'), ('L', 'Solo Lectura')], default='L', max_length=1)),
            ],
        ),
    ]
