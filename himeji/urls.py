from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Forum/', include('Forum.urls', namespace='forum')),
    path('', include('website.urls', namespace='website')),
]
