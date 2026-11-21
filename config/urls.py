
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)