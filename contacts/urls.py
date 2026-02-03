from django.contrib import admin
from django.urls import path
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.ContactBookHome, name='home'),

    path('updateContactForm/', views.updateContactForm, name='updateContactForm'),
    path('updateContact/', views.updateContact, name='updateContact'),
    path('searchContact/', views.searchContact, name='searchContact'),
    path('deleteContact/', views.deleteContact, name='deleteContact'),
]
