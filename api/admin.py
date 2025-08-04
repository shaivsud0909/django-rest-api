from django.contrib import admin

# Register your models here.

from api.models import Company, Worker

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'established_date',)
    search_fields = ('name', 'location')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','Company',)
    search_fields = ('name', 'Company__name',)  
    list_filter = ('Company',)  # Filter by company   

admin.site.register(Company, CompanyAdmin)
admin.site.register(Worker, WorkerAdmin)
