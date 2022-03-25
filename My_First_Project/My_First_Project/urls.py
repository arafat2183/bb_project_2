from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('first_app/', include('first_app.urls')),
]
