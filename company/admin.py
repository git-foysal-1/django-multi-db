from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'employees')
    search_fields = ('name',)


admin.site.register(Company, CompanyAdmin)
