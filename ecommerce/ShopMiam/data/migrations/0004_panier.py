# Generated by Django 4.1 on 2022-09-05 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_usercreation_statut_alter_annonces_auteur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1)),
                ('statut', models.BooleanField(default=False)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.annonces')),
            ],
        ),
    ]
