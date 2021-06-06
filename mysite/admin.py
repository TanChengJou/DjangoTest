from django.contrib import admin
from .models import NewTable,Product
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','qty','price')



admin.site.register(NewTable)
admin.site.register(Product,PostAdmin)
