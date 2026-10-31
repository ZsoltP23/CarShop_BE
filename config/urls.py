
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from ShopMain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.view_home, name="HomePage"),
    path('des/', views.view_des, name="DescriptionName"),
    path('des/<int:pk>/', views.view_des_id),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/register/', views.RegisterView.as_view()),
]
