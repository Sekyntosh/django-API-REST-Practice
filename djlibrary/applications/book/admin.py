from django.contrib import admin

# Register your models here.

from .models import Autor, Publisher , Book

admin.site.register(Autor)
admin.site.register(Publisher)
admin.site.register(Book)