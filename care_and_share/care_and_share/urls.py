"""care_and_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app.views import LandingPage, AddDonation, Login, Register, Logout, UserDetails, Confirmation, UserDetailsUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', LandingPage.as_view(), name='LandingPage' ),
    path('share/', AddDonation.as_view(), name='AddDonation'),
    path('login/', Login.as_view(), name='Login'),
    path('register/', Register.as_view(), name='Register'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('user_details/<int:pk>/', UserDetails.as_view(), name='User Details'),
    path('confirmation/', Confirmation.as_view(), name='Confirmation'),
    path('user_update/<int:pk>/', UserDetailsUpdate.as_view(), name='User Details Update'),
]