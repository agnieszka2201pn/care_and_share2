from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DetailView

from accounts.models import CustomUser
from main_app.forms import RegisterForm
from main_app.models import Institution, Donation, Category


class LandingPage(View):
    def get(self,request):
        user = request.user
        donations = Donation.objects.all()
        bags_count = 0
        for donation in donations:
            bags_count += donation.quantity
        organizations_count = Institution.objects.count()
        foundations = Institution.objects.filter(type=0)
        ngos = Institution.objects.filter(type=1)
        foundraisings = Institution.objects.filter(type=2)
        context = {'bags_count':bags_count,
                   'organizations_count':organizations_count,
                   'foundations':foundations,
                   'ngos':ngos,
                   'foundraisings':foundraisings,
                   'user':user,
                   }
        return render(request, 'main_app/index.html', context)


class AddDonation(View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        user = request.user
        if user.is_authenticated:
            context = {'user':user, 'categories':categories, 'institutions':institutions}
            return render(request, 'main_app/form.html', context)
        else:
            return HttpResponse('załóż konto lub zaloguj się')


class Login(View):
    def get(self, request):
        return render(request, 'main_app/login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user1 = authenticate(email=email,password=password)
        if user1:
            login(request,user1)
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/register/')


class Logout(View):
    def get(self,request):
        return render(request, 'main_app/logout.html')

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/index/')

# class Register(View):
#     def get(self, request):
#         return render(request, 'main_app/register.html')


class Register(FormView):
    template_name = 'main_app/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('Login')
    def form_valid(self, form):
        cd = form.cleaned_data
        user = CustomUser.objects.create(first_name=cd['first_name'], surname=cd['surname'], email=cd['email'])
        user.set_password(cd['password'])
        user.save()
        return super().form_valid(form)


class UserDetails(DetailView):
    model = CustomUser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user.pk'] = self.kwargs['pk']
        return context




