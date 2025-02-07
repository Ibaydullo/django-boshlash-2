from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdeteView,
    BlogDeleteView,
)

urlpatterns = [

    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdeteView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('',BlogListView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]