from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost, BlogCategory


class BlogListView(ListView):
    model = BlogPost
    template_name = 'about_caffee.html'  # همین تمپلیت
    context_object_name = 'posts'
    queryset = BlogPost.objects.select_related('category').order_by('-created_at')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'detail_caffee.html'  # اینجا template جزئیات
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'