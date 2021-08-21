from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addLibrarian,name='addLibrarian'),
    path('viewall/', views.viewLibrarian,name='viewLibrarian'),
    path('view/<id>', views.librarianDetails,name='librarianDetails'),
    path('enroll_code/<ecode>', views.singleLibrarian,name='singleLibrarian'),
    path('register/', views.LibrarianPage,name='LibrarianPage'),
    path('login/', views.Librarianlogin,name='Librarianlogin'),
]