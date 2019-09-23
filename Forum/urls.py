from . import views
from django.urls import path


app_name = 'forum'
urlpatterns = [
    path('', views.Base.as_view(), name='forum')
]