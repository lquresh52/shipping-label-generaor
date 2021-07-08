from django.urls import path, include
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('home/',views.home, name='home'),
    path('history/', views.history, name='history'),
    path('generate-new-label/', views.generate_new_label, name='generate-new-label'),
    path('edit-label/<int:id>/', views.edit_label, name='edit-label'),
    path('delete-label/<int:id>/', views.delete_label, name='delete-label'),
    path('print-label/<int:id>/', views.print_label, name='print-label'),
    path('logout/', views.logout, name='logout'),
    
]
