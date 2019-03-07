from django.urls import path
from . import views

urlpatterns = \
    [
        path('',views.index,name='index'),
        path('AboutUs/',views.AboutUs,name='AboutUs'),
        path('Gallery/',views.Gallery,name='Gallery'),
        path('Resources/',views.Resources,name='Resources'),
        path('ContactUs/',views.ContactUs,name='ContactUs'),
        path('SecretPage/',views.SecretPage,name='SecretPage')
    ]