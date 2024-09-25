from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from game_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/games/', views.games_list),
    path('api/events/', views.events_list),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
