from . import views
from django.urls import path


app_name = 'website'
urlpatterns = [
    path('', views.AllList.as_view(), name='home'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.PostList.as_view(), name='news'),
    path('knowledge/', views.KnowledgeList.as_view(), name='knowledge'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]