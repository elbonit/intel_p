

from django.urls import path
from app.views import index, detail,checkoutt,confirmation,conf

urlpatterns = [

    path('', index, name='home'),
    path('<int:myid>', detail,name="detail"),
    path('checkoutt', checkoutt,name="checkoutt"),
    path('confirmation', conf,name="confirmation"),
    path('conf', conf,name="conf"),
]