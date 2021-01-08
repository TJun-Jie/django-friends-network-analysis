import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','network_project.settings')

import django
django.setup()

#Fake script

import random 
from main_app.models import Student, Friendship
from faker import Faker

fakegen =Faker()

def add_student(N=5):
    for entry in range(N):
        student = fakegen.name()
        
        stu = Student.objects.get_or_create(name =student)[0]

        
        
# def add_friendship():
    
if __name__ =='__main__':
    print('populating script!')
    add_student()
    print("Populating complete!")