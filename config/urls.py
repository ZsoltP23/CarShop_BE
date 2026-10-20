
from django.contrib import admin
from django.urls import path
from ShopMain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.view_home),
    path('des/', views.view_des),
]
