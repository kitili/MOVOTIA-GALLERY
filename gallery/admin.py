from django.contrib import admin
from .models import photos
from .models import Category,Image,Location

admin.site.register(photos)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Location)
