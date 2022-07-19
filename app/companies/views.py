from django.shortcuts import render, get_object_or_404
from .models import Company, Employee, More

# Create your views here.
def index(request):
    company_list= Company.objects.all()
    context= {
        'company_list':company_list
    }
    return render(request, 'companies/index.html', context)

def employees(request, company_id):
    company_get= Company.objects.get(id=company_id)
    employee_list= company_get.employee.all()
    #print(employee_list)
    context= {
        'company_get':company_get,
        'employee_list':employee_list,
    }
    return render(request, 'companies/employees.html', context)

def detail(request, employee_id):
    employee_get=Employee.objects.get(id=employee_id)
    detail_list= employee_get.more.all()
    context= {
        'employee_get':employee_get,
        'detail_list':detail_list,
    }
    return render(request, 'companies/detail.html', context)