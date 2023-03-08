from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]