from django.urls import path
from . import views
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "blog_ra68"
app_name= "blog"
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # ← This is your homepage
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category_posts'),
    ]
