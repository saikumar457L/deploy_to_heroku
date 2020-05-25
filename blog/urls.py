from django.urls import path

from .views import PostListView,PostDetailView,AddPost
from .views import EditPost,DeletePost

app_name = "blog"

urlpatterns = [
    path("",PostListView.as_view(), name = "home"),
    path("<int:pk>/",PostDetailView.as_view(), name = "detail"),
    path("newpost/",AddPost.as_view(), name="newpost"),
    path("<int:pk>/edit/",EditPost.as_view(), name="editpost"),
    path("<int:pk>/delete/",DeletePost.as_view(), name="deletepost"),
    

]
