from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addDoctor,name='addDoctor'),
    path('viewall/', views.viewDoctors,name='viewDoctors'),
    path('view/<id>', views.doctorDetails,name='doctorDetails'),
    path('search/', views.searchapi,name='searchapi'),
    path('update/', views.update_api,name='update_api'),
    path('update_data/', views.update_dataread,name='update_dataread'),
    path('delete/', views.delete_api,name='delete_api'),
    path('delete_data/', views.delete_dataread,name='delete_dataread'),
    path('login_check/', views.login_check,name='login_check'),

    path('page/', views.doctorAdd,name='doctorAdd'),
    path('viewdoctorpage/', views.viewingDoctors,name='viewingDoctors'),
    path('searchdoctorpage/', views.searchDoctor,name='searchDoctor'),
    path('updatedoctorpage/', views.updateDoctor,name='updateDoctor'),
    path('deletedoctorpage/', views.deleteDoctor,name='deleteDoctor'),
    path('login/', views.loginData,name='loginData'),
  
]