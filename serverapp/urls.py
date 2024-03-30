from django.urls import path

from serverapp import views

urlpatterns = [
    path('tables/', views.tables, name='tables')
]