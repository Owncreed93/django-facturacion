from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
)

# Create your views here.

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser

        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        
        return HttpResponseRedirect( reverse_lazy(self.login_url) )
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

class HomeSinPrivilegios(LoginRequiredMixin, TemplateView):
    login_url = 'bases:login'
    template_name = 'bases/sin_privilegios.html'


class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, CreateView):
    context_object_name = 'obj'
    success_message = 'Registro agregado satisfactoriamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    context_object_name = 'obj'
    success_message = 'Registro actualizado satisfactoriamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)