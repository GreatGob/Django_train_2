from django.urls import path
from . import views

app_name= 'companies'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:company_id>/employees/', views.employees, name='employees'),
    path('<int:company_id>/employees/<int:employee_id>/', views.detail, name='detail'),
]
