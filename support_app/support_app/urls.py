from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('admin/', admin.site.urls),
    path('', include('questions.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
