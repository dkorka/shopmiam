
from django.forms import ModelForm
from .models import Annonces, Usercreation, Panier
from django.contrib.auth.forms import UserCreationForm


class Usercreation_form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Usercreation
        fields = UserCreationForm.Meta.fields + ('email','last_name','age','statut')
    

class Annonces_form(ModelForm):
    class Meta:
        model=Annonces
        fields=['slug','titre','description','piece_jointe','prix']


class Panier_form(ModelForm):
    class Meta:
        model=Panier
        fields=['quantite']

