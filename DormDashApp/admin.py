from django.contrib import admin

# Register your models here.

from .models import *
from .models import Profile

admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Profile)
admin.site.register(Restaurant)