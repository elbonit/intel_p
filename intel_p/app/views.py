from django.shortcuts import render
from .models import Produit,commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    produit_object= Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        produit_object= Produit.objects.filter(nom__icontains=item_name)
    paginator=Paginator(produit_object,4)
    page= request.GET.get('page')
    produit_object=paginator.get_page(page)
    return render(request, 'app/index.html',{'produit_object':produit_object })



def detail(request,myid):
    produit_object=Produit.objects.get(id=myid)
    return render(request, 'app/detail.html',{'produit_object':produit_object })

def checkoutt(request):
    if request.method =="POST":
        items = request.POST.get('items')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays= request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = commande(nom=nom, email=email,adresse=adresse,ville=ville,pays=pays,items=items,zipcode=zipcode)
        com.save()
    return render(request, 'app/checkoutt.html')


def conf (request):
    info = commande.objects.all()[:1]
    for item in info:
        nom= item.nom
    return render(request, 'app/conf.html',{'nom':nom})

def confirmation(request):
    return render(request, 'app/conf.html')
