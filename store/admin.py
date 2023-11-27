from django.contrib import admin
from .models import *

admin.site.site_header = 'Ecommerce Administration'
admin.site.site_title = 'Administration'
admin.site.index_title = 'E-Commerce'

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)