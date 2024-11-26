from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="blog-home"),
    path("latest-posts/", views.LatestPostListView.as_view(), name="latest-posts"),
    path("user/<str:username>", views.UserPostListView.as_view(), name="user_posts"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/new", views.PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog-about"),
]
