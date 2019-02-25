from django.urls import path
from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_list, name='lists'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.contact_delete, name='delete'),
]