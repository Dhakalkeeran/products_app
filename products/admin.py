from django.contrib import admin
from .models import Category, Tag, Product

# Register models to admin dashboard
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)