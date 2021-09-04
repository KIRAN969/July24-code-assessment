from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addPatient,name='addPatient'),
    path('viewall/', views.viewPatients,name='viewPatients'),
    path('view/<id>', views.patientDetails,name='patientDetails'),
    path('search/', views.searchapi,name='searchapi'),
    path('update/', views.update_searchapi,name='update_searchapi'),
    path('update_data/', views.update_data_read,name='update_data_read'),
    path('delete/', views.delete_searchapi,name='delete_searchapi'),
    path('delete_data/', views.delete_data_read,name='delete_data_read'),
    path('login_check/', views.login_check,name='login_check'),



    path('page/', views.patientAdd,name='patientAdd'),
    path('viewpatientpage/', views.viewingPatients,name='viewingPatients'),
    path('searchpatientpage/', views.patientSearch,name='patientSearch'),
    path('updatepatientpage/', views.patientUpdate,name='patientUpdate'),
    path('deletepatientpage/', views.patientDelete,name='patientDelete'),
    path('login/', views.loginData,name='loginData'),

  
]