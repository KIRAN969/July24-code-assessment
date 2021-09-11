from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.addStudent,name='addStudent'),
    path('viewall/', views.viewStudents,name='viewStudents'),
    path('view/<id>', views.studentDetails,name='studentDetails'),
    path('login_check/', views.login_check,name='login_check'),
    path('update_data/', views.update_dataread,name='update_dataread'),





    path('page/', views.StudentAdd,name='StudentAdd'),
    path('viewstudentpage/', views.viewingStudent,name='viewingStudent'),
    path('login/', views.loginData,name='loginData'),
    path('profilepage/', views.ProfileData,name='ProfileData'),
    path('updatepage/', views.EditProfile,name='EditProfile'),




  
]