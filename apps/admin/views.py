from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.admin.forms import AdminAuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login

from apps.core.views import AdminRequiredMixin
# Create your views here.

class DashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/dashboard_index.html'

class LoginView(FormView):
    template_name = 'admin/login.html'
    form_class = AdminAuthenticationForm

    def get(self. request, *args, **kwargs):
        user = request.user
        if user.is_active() and user_is_staff():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self,request, admin)
        return super().form_valid(form)
