from django.contrib import admin
from mysiteApp.models import Contact, Newsletter

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    


admin.site.register(Newsletter)