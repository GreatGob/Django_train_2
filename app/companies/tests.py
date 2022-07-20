from time import time
from django.utils import timezone
from django.test import TestCase
from .models import Company, Employee, More
import datetime

# Create your tests here.
def company_create(c_name, days):
    time= timezone.now() + datetime.timedelta(days=days)
    return Company.objects.create(c_name= c_name, pub_date= time)
class CompanyModelTests(TestCase):
    pass


def employee_create(e_name, days):
    time= timezone.now() + datetime.timedelta(days=days)
    return Employee.objects.create(e_name=e_name, pub_date= time)
class EmployeeModelTests(TestCase):
    pass

def information_create(first_name, last_name, age, days):
    time= timezone.now() + datetime.timedelta(days=days)
    return More.objects.create(first_name=first_name, last_name=last_name, age= age, pub_date= time)
class MoreModelTests(TestCase):
    pass