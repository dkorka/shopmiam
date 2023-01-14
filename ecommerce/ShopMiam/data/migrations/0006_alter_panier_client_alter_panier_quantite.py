# Generated by Django 4.1 on 2022-09-06 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_panier_client_alter_panier_quantite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panier',
            name='client',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='panier',
            name='quantite',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=4, max_length=1),
        ),
    ]