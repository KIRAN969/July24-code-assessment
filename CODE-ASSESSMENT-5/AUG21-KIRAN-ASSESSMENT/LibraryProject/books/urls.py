from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addBook,name='addBook'),
    path('viewall/', views.viewBooks,name='viewBooks'),
    path('view/<id>', views.bookDetails,name='bookDetails'),
    path('name/<book>', views.singlebook,name='singlebook'),
    path('', views.BookPage,name='BookPage'),
]