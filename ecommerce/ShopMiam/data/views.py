
from django.shortcuts import render, redirect
from .models import Annonces, Usercreation, Panier
from .annonce_form import Annonces_form,Usercreation_form,Panier_form


def inscription_fonc(request):
    error=''
    if request.method == 'POST':
        formulaire=Usercreation_form(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            return redirect('index_name')
        else:
            error=formulaire.errors
    formulaire=Usercreation_form()
    return render(request,'inscription.html',context={'formulaire':formulaire, 'error':error})



def mes_annonces(request):

    if request.user.is_authenticated and  request.user.statut =='Vendeur':
        annonces_utilisateur=[]
        for elt in Annonces.objects.all():
            if elt.auteur_id == request.user.id:
                annonces_utilisateur.append(elt)
        return render(request,'mes_annonces.html', context={"annonces_utilisateur":annonces_utilisateur})
    return redirect('index_name')



def ajout_annonce(request):
    error=''
    if request.user.is_authenticated and request.user.statut=='Vendeur':
        if request.method == 'POST':
            formulaire=Annonces_form(request.POST, request.FILES)
            if formulaire.is_valid():
                Annonces.objects.create(slug=formulaire.cleaned_data['slug'],
                titre=formulaire.cleaned_data['titre'],description=formulaire.cleaned_data['description'],
                piece_jointe=formulaire.cleaned_data['piece_jointe'],auteur=Usercreation.objects.get(id=request.user.id), prix=formulaire.cleaned_data['prix'])
                
                return redirect('index_name')
            else:
                error=formulaire.errors
        formulaire=Annonces_form()
        return render(request,'ajout_annonce.html', context={'formulaire':formulaire, 'error':error})



def modifier_annonce(request, slug_modif_annonce):
    
    try:
        annonce=Annonces.objects.get(slug=slug_modif_annonce)
        initial={'slug':annonce.slug, 'titre':annonce.titre,'description':annonce.description,'piece_jointe':annonce.piece_jointe,'prix':annonce.prix}
        if (request.user.is_authenticated)   and  (annonce.auteur_id == request.user.id):
            if request.method =='POST':
                form=Annonces_form(request.POST, request.FILES, initial=initial)
                
                if form.is_valid():
        
                    annonce.slug=form.cleaned_data['slug']
                    annonce.titre=form.cleaned_data['titre']
                    annonce.description=form.cleaned_data['description']
                    annonce.piece_jointe=form.cleaned_data['piece_jointe']
                    annonce.prix=form.cleaned_data['prix']
                    annonce.save()
                    
                    return redirect('mes_annonces_name')
                return render(request,'modif_annonce.html', context={'form':form, 'errors':form.errors})

            form=Annonces_form(initial=initial)
            return render(request,'modif_annonce.html', context={'form':form})  
    except:
        return render('index_name')



def supprimer_annonce(request, slug_suppression):
    
    for annonce in Annonces.objects.all():
        if request.user.is_authenticated and annonce.slug == slug_suppression and annonce.auteur_id ==request.user.id:
            annonce.delete()
    return redirect('mes_annonces_name')


def sous_total(request):
    sous_total=0
    for elt in npanier(request)[1]:

        sous_total_ref=float(Panier.objects.get(reference_id=elt, client_id=request.user.id).quantite) * float(Annonces.objects.get(id=elt).prix)
        sous_total+=sous_total_ref
    return sous_total

    
def details_panier_fonc(request):
    liste_couple=[]
    for elt in npanier(request)[0]:
        qtte=Panier.objects.get(reference_id=elt.id, client_id=request.user.id).quantite
        liste_couple.append({"ref":elt,'prix':elt.prix,'nombre_article':qtte})
    return render(request,'panier.html',context={'details_panier':liste_couple,'nombre_ref_panier':npanier(request)[2],'sous_total':sous_total(request)})


            
            

def npanier(request):  #liste des références dans le panier du client connecté à partir du model 'Annonce'
    liste_ref_annonce=[] # liste des référence mises dans le panier par le client
    liste_reference_id=[]  # pour verifier si la ref est listé et eviter un doublon
    nombre_total_reference=0
    for elt in Panier.objects.all():
        annonce=Annonces.objects.get(id=elt.reference_id)
        if elt.client_id == request.user.id  and elt.statut == False and elt.reference_id not in liste_reference_id :
            liste_reference_id.append(elt.reference_id)

            liste_ref_annonce.append(annonce)

    for elt in liste_reference_id:
        n=Panier.objects.get(reference_id=elt, client_id=request.user.id).quantite
        nombre_total_reference+=int(n)
        
    return [liste_ref_annonce,liste_reference_id, nombre_total_reference]


def details_annonce(request,slug_request): # Affiche detail de la ref + ajout dans le panier
    for elt in Annonces.objects.all():
        if elt.slug == slug_request:
            if request.method == 'POST':
                form=Panier_form(request.POST)  #pour enregistrer la quantité
                if form.is_valid():
                    qtt=form.cleaned_data['quantite']
                    ref=Annonces.objects.get(id=elt.id)
                    client=Usercreation.objects.get(id=request.user.id)
                    for elt_panier in Panier.objects.all():
                        if elt_panier.reference_id==elt.id and elt_panier.client_id==request.user.id:
                            elt_panier.quantite =qtt
                            elt_panier.save()
                            return redirect('mon_panier_name')
                        
                    Panier.objects.create(quantite=qtt, reference=ref, client=client)
                    return redirect('index_name')

            elif elt.id in npanier(request)[1]: #Vérifie si la référence est dans le panier du clients
                qtt=Panier.objects.get(reference_id=elt.id, client_id=request.user.id).quantite # recupere la valeur quantite de la reference dans le panier
                return render (request, 'details_annonce.html', context={'annonce':elt, 'choix_nombre_article':Panier_form(initial={"quantite":qtt}), 'nombre_ref_panier':npanier(request)[2], 'sous_total':sous_total(request)})
            else: # si la référence n'existe pas dans le panier on retourne un formulaire normale avc quantite egale 1 par defaut
                return render (request, 'details_annonce.html', context={'annonce':elt, 'choix_nombre_article':Panier_form(), 'nombre_ref_panier':npanier(request)[2],'sous_total':sous_total(request)})
    return redirect('index_name')

            
def annulation(request,slug_request_annule):
    for elt in Annonces.objects.all():
        if elt.slug==slug_request_annule:
            a=Panier.objects.get(reference_id=elt.id, client_id=request.user.id)
            a.delete()
    return redirect('mon_panier_name')