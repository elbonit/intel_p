from django.contrib import admin
from .models import Categorie,Produit,Service,commande

# Register your models here.
admin.site.site_header = "INTELCORATION"
admin.site.index_title = "LE PATRON"
class Admincategorie(admin.ModelAdmin):
    list_display = ('nom','date_ajout')
class AdminProduit(admin.ModelAdmin):
    list_display = ('nom','prix','categorie','date_ajout')
class AdminService(admin.ModelAdmin):
    list_display = ('nom','date_ajout','prix','description')
class Admincommande(admin.ModelAdmin):
    list_display = ('items' , 'nom' ,'email','adresse', 'ville','pays','zipcode','date_commande')
admin.site.register(Categorie,Admincategorie)
admin.site.register(Produit,AdminProduit)
admin.site.register(Service,AdminService)
admin.site.register(commande,Admincommande)
