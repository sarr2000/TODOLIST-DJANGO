
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import  User,Group
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import ListView,CreateView,DetailView,DeleteView
from django.urls import reverse_lazy
from .forms import CreateUserForm


# Create your models here.

class RegisterView(View):

    template_name = 'compte/register.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)

    def post(self,request, *args ,**Kwargs):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'utilsateur existe déja')

            else:

                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                group = Group.objects.get(name='Standard')
                user.groups.add(group)
                user.save()
                messages.success(request,'Compte créé avec succés')

        else:
             messages.error((request,'mots de passes non identiques'))
        return render(request,self.template_name)



class LoginView(View):
    template_name ='compte/login.html'

    def get(self,request,*args, **Kwargs):
        return  render(request,self.template_name)

    def post(self,request,*args, **Kwargs):
        username =request.POST.get('username')
        password = request.POST.get('password')


        user =authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'connexion réussie')
        else:
            messages.error(request,'verifier les parametres de connexion')

        return render(request,self.template_name)


def logoutView(request):
   logout(request)
   messages.success(request,'déconnexion réussie')
   return redirect('compte:login')



class UserListView(ListView):
    model = User
    context_object_name = "liste_users"
    template_name = "compte/user_list_view.html"

class UserCreateview(CreateView):
    model =  User
    template_name = "compte/register.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("compte:users")















