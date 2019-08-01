import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobportal.settings')
import django
django.setup()

from jp001.models import indiaJob,indiaJob1,indiaJob2,indiaJob3
from faker import Faker
from random import *
fake=Faker()

def phonenumgen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))

    return int(num)



def populate(n):
    for i in range(n):
        fempname=fake.name()
        fempexp=fake.random_int(min=1,max=20)
        fempskills=fake.random.choice(('Devops','Python','C','C++','Linux'))
        fempphone=phonenumgen()
        emp_record=indiaJob.objects.get_or_create(empname=fempname,empskills=fempskills,empexp=fempexp,empphone=fempphone)
        emp_record=indiaJob1.objects.get_or_create(empname=fempname,empskills=fempskills,empexp=fempexp,empphone=fempphone)
        emp_record=indiaJob2.objects.get_or_create(empname=fempname,empskills=fempskills,empexp=fempexp,empphone=fempphone)
        emp_record=indiaJob3.objects.get_or_create(empname=fempname,empskills=fempskills,empexp=fempexp,empphone=fempphone)
populate(20)
