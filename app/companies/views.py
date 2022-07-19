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
    employee_list= Employee.objects.filter(company_id=company_id)
    company= get_object_or_404(Company, pk= company_id)
    #print(employee_list)
    context= {
        'employee_list':employee_list,
        'company':company,
    }
    return render(request, 'companies/employees.html', context)

def detail(request, employee_id, company_id):
    detail_list=More.objects.filter(employee_id=employee_id)
    employee= get_object_or_404(Employee, pk= employee_id)
    company=employees(company_id)
    context= {
        'employee':employee,
        'company': company,
        'detail_list':detail_list,
    }
    return render(request, 'companies/detail.html', context)