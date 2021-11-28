from django.contrib import admin

from accounts.models import CustomUser
from main_app.models import Institution

admin.site.register(CustomUser)
admin.site.register(Institution)
