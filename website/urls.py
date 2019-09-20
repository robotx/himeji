from . import views
from django.urls import path


urlpatterns = [
    path('', views.AllList.as_view(), name='home'),
    path('news/', views.PostList.as_view(), name='news'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('knowledge/', views.KnowledgeList.as_view(), name='knowledge'),
]