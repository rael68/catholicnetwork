from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    return render(request, "blog_ra68/index.html")
from django.shortcuts import get_object_or_404


# blog_ra68/views.py
from django.views.generic import ListView
from .models import Post, Category

from django.shortcuts import get_object_or_404

# blog_ra68/views.py
from django.views.generic import DetailView
from django.utils.html import strip_tags

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_ra68/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Post.objects.filter(status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = strip_tags(self.object.content)
        word_count = len(content.split())
        read_time = (word_count + 199) // 200  # Round up: 200 wpm
        context['word_count'] = word_count
        context['read_time'] = read_time
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog_ra68/post_list.html'   # <-- NEW
    context_object_name = 'posts'
    paginate_by = 12
    ordering = ['-publish_date']

    def get_queryset(self):
        qs = Post.objects.filter(status='published').select_related('author', 'category')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(content__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.annotate(count=models.Count('post')).filter(count__gt=0)
        ctx['recent_posts'] = Post.objects.filter(status='published')[:5]
        return ctx

class CategoryListView(ListView):
    model = Post
    template_name = 'blog_ra68/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category, status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context 
