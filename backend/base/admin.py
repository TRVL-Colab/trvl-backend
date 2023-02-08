from django.contrib import admin
from .models import Trip, Destination, Transportation, Document, Photo, Country, City, State

# Register your models here.
admin.site.register(Trip)
admin.site.register(Destination)
admin.site.register(Transportation)
admin.site.register(Document)
admin.site.register(Photo)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)