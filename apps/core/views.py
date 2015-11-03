from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

# Create your views here.

class AdminRequiredMixin(object):
    @method_decorator(permission_required('is_superuser', login_url='/admin/login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
