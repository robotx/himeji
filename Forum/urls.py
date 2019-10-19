from . import views
from django.urls import path, include
from django.contrib import admin


app_name = 'forum'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', views.Base.as_view(), name='forum'),
]