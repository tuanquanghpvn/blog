from django.shortcuts import render 
from django.views.generic import (
    TemplateView, CreateView, UpdateView, 
    DeleteView, FormView, ListView
)
from django.contrib.admin.forms import AdminAuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login

from apps.core.views import AdminRequiredMixin
from apps.categories.models import Category
from apps.posts.models import Post
from apps.products.models import Products
from apps.tags.models import Tag

class DashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Dashboard Home',
                'sidebar': ['dashboard']
            }
        }
        context.update(info)
        return context

class LoginView(FormView):
    template_name = 'admin/login.html'
    form_class = AdminAuthenticationForm

    def get(self, request, *args, **kwargs):
        user = request.user
        if (user.is_active and user.is_staff) or user.is_superuser:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)

class CategoryListView(AdminRequiredMixin, ListView):
    template_name = 'admin/category_list.html'
    model = Category

    def get_context_data(self, **kwagrs):
        context = super().get_context_data(**kwagrs)
        info = {
            'info': {
                'title': 'List Category',
                'sidebar': ['parent_post', 'category'],
            }                            
        }
        context.update(info)
        return context

class CategoryCreateView(AdminRequiredMixin, CreateView):
    template_name = 'admin/category_create.html'
    model = Category
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Create Category',
                'sidebar': ['parent_post', 'category'],
            }                            
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:category_list')

class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'admin/category_update.html'
    model = Category
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Update Post Category',
                'sidebar': ['parent_post', 'category'],
            }                            
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:category_list')
   
class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for CategoryPostDeleteView"""
    model = Category

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:category_list')

class PostListView(AdminRequiredMixin, ListView):
    """docstring for PostListView"""
    model = Post
    template_name = 'admin/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Post List',
                'sidebar': ['parent_post', 'post'],
            },
        }
        context.update(info)
        return context

class PostCreateView(AdminRequiredMixin, CreateView):
    model = Post
    template_name = 'admin/post_create.html'
    fields = ('name', 'slug', 'description', 
               'content', 'image', 'category',)

    def get_context_data(self, **kwargs):
        info = {
            'info': {
                'title': 'Post Create',
                'sidebar': ['parent_post', 'post'],
            },
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:post_list')

class PostUpdateView(AdminRequiredMixin, UpdateView):
    model = Post
    template_name = 'admin/post_update.html'
    fields = ('name', 'slug', 'description',
               'content', 'image', 'category',)

    def get_context_data(self, **kwargs):
        info = {
            'info': {
                'title': 'Post Update',
                'sidebar': ['parent_post', 'post'],
            },
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:post_list')

class PostDeleteView(AdminRequiredMixin, DeleteView):
    model = Post

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:post_list')

class TagListView(AdminRequiredMixin, ListView):
    model = Tag
    template_name = 'admin/tag_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Tag List',
                'sidebar': ['parent_post', 'tag'],
            },
        }
        context.update(info)
        return context

class TagCreateView(AdminRequiredMixin, CreateView):
    model = Tag
    template_name = 'admin/tag_create.html'
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Tag Create',
                'sidebar': ['parent_post', 'tag'],
            },
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:tag_list')

class TagUpdateView(AdminRequiredMixin, UpdateView):
    model = Tag
    template_name = 'admin/tag_update.html'
    fields = ('name', 'slug', 'description',)

    def get_context_data(self, **kwargs):
        context = super().get_contex_data(**kwargs)
        info = {
            'info': {
                'title': 'Tag Update',
                'sidebar': ['parent_post', 'tag'],
            },
        }
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('admin:tag_list')

class TagDeleteView(AdminRequiredMixin, DeleteView):
    model = Tag
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:tag_list')
