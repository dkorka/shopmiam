from django.shortcuts import render
from data.models import Annonces
from data.views import npanier, sous_total
from django.core.paginator import Paginator

def index_page(request):
    try:
        search=request.GET.get('search')
        all_annonces=Annonces.objects.filter(titre__icontains=search)

    except:
        all_annonces=Annonces.objects.all()

    nombre_article=all_annonces.count()
    paginator=Paginator(all_annonces,8)
    page_number=request.GET.get('page',1)
    page_object=paginator.get_page(page_number)
    
    return render(request,'index.html',context={"page_object":page_object, 'nombre_ref_panier':npanier(request)[2],'sous_total':sous_total(request),'nombre_article':nombre_article})

""