from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:patient_id>/', views.detail, name='detail'),
    path('<int:patient_id>/edit/', views.edit, name='edit'),
    path('<int:patient_id>/delete/', views.delete, name='delete'),
]