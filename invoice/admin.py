from django.contrib import admin

# Register your models here.

from .models import Invoice,Transaction

admin.site.register(Invoice)
admin.site.register(Transaction)
