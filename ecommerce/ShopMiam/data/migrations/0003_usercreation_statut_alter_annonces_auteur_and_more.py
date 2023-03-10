# Generated by Django 4.1 on 2022-08-27 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_usercreation_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreation',
            name='statut',
            field=models.CharField(choices=[('Acheteur', 'Acheteur'), ('Vendeur', 'Vendeur')], default='Acheteur', max_length=8),
        ),
        migrations.AlterField(
            model_name='annonces',
            name='auteur',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
