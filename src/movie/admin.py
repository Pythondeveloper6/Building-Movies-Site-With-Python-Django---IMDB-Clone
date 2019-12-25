from django.contrib import admin

# Register your models here.
from .models import Movie , MovieLinks



admin.site.register(Movie)
admin.site.register(MovieLinks)