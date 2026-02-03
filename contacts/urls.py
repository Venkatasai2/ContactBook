from django.urls import path
from . import views


urlpatterns = [

    path('ContactBookHome',views.ContactBookHome,name='ContactBookHome'),
    path('updateContactForm',views.updateContactForm,name='updateContactForm'),
    path('updateContact',views.updateContact,name='updateContact'),
    path('searchContact',views.searchContact,name='searchContact'),
    path('deleteContact',views.deleteContact,name='deleteContact')
]