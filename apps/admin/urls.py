from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.DashboardView.as_view(), name='dashboard'),
        url(r'^login/', views.LoginView.as_view(), name='login'),
]
