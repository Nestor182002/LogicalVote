# views
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

# redirects
from django.urls import reverse_lazy
from django.shortcuts import redirect

# form register
from django.views.generic.edit import FormView
from Users.form import UserRegisterForm

# login y register views
class UserLogin(LoginView):
    template_name = "login.html"
    fiels = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('votes')

class RegisterView(FormView):
    template_name="register.html"
    form_class = UserRegisterForm
    redirect_authenticated_user=True
    success_url=reverse_lazy("login")

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            return super(RegisterView,self).form_valid(form)
    
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/Inicio')
        else:
            return super().dispatch(*args, **kwargs)
        return super().dispatch(*args, **kwargs)


class templateInicio(TemplateView):
    template_name="inicio.html"