from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView, ListView
from django.contrib.admin.forms import AdminAuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login

from apps.core.views import AdminRequiredMixin
from apps.categories.models import Category
from apps.posts.models import Post
from apps.products.models import Products
# Create your views here.

class DashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/dashboard_index.html'

class LoginView(FormView):
    template_name = 'admin/login.html'
    form_class = AdminAuthenticationForm

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
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
                     
                        }                            
                            }
