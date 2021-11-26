from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from main_app.forms import RegisterForm
from main_app.models import Institution, Donation


class LandingPage(View):
    def get(self,request):
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
                   }
        return render(request, 'main_app/index.html', context)


class AddDonation(View):
    def get(self, request):
        return render(request, 'main_app/form.html')


class Login(View):
    def get(self, request):
        return render(request, 'main_app/login.html')


# class Register(View):
#     def get(self, request):
#         return render(request, 'main_app/register.html')


class Register(FormView):
    template_name = 'main_app/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('Login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




