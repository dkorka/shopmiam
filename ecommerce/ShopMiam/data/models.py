from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Usercreation(AbstractUser):
    choix=[("Acheteur","Acheteur"),("Vendeur","Vendeur")]

    age=models.IntegerField()
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)
    statut=models.CharField(max_length=8,choices=choix, default='Acheteur')



class Annonces(models.Model): 
    slug=models.CharField(max_length=20, unique=True, default='')
    titre=models.CharField(max_length=20)
    description=models.TextField()
    piece_jointe=models.ImageField()
    prix=models.PositiveIntegerField(default=0)
    date_pub=models.DateTimeField(auto_now_add=True)
    auteur=models.ForeignKey(get_user_model(), on_delete= models.PROTECT, default=2)


class Panier(models.Model):
    qtte=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")]

    reference=models.ForeignKey(Annonces, on_delete=models.CASCADE)
    client=models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=4)
    quantite=models.CharField(max_length=1, choices=qtte, default=1)
    statut=models.BooleanField(default=False)