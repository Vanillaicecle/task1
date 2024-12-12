from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('task1/admin/', admin.site.urls),  # Админка через префикс
    path('task1/', include('tasks.urls')),  # Все маршруты приложения
    path('task1/accounts/', include('django.contrib.auth.urls')),  # Аутентификация через префикс
]