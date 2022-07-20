from django.contrib import admin
from .models import Company, Employee,More
# Register your models here.

class MoreInLine(admin.TabularInline):
    model= More
    extra= 3
class EmployeeInLine(admin.TabularInline):
    model= Employee
    extra= 3    
class EmployeeAmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields':['e_name']}),
        ('Data information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    list_display=('e_name', 'pub_date', 'was_published_recently')
    list_filter= ['pub_date']
    search_fields=['e_name']
    
    inlines=[MoreInLine]
class CompanyAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields': ['c_name']}),
        ('Data information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    list_display= ('c_name', 'pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['c_name']
    
    inlines= [EmployeeInLine]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAmin)
admin.site.register(More)