from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)
admin.site.register(Image)