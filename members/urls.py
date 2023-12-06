from django.urls import path
from . import views

urlpatterns= [
    path('upload/',views.upload_csv,name='upload_csv'),
    path('upload/success/',views.upload_success,name='upload_success'),
    path('show/', views.show_csv,name='show_csv'),
]