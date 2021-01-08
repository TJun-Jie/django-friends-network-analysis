import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','network_project.settings')

import django
django.setup()

#Fake script

import random 
from main_app.models import Student, Friendship1
from faker import Faker

fakegen =Faker()
# seed to generate 10 students
def add_student(N=10):
    for entry in range(N):
        student = fakegen.name()
        
        stu = Student.objects.get_or_create(name =student)[0]

        
# seed to add 2 friends for each student while selecting a popular kid
# every student will choose the popular student as their friend (except the popular student himself)
# other than that the student will choose his own friend
def add_friendship():
    number_of_students = Student.objects.all().count()

    popular_kid_id = 3
    popular_kid = Student.objects.get(pk=popular_kid_id)

    for i in range(number_of_students):
        student = Student.objects.get(pk=i+1)
        if(student):
            # add popular kid as friend 
            if( i != popular_kid_id-1):
                friendship  = Friendship1( student = student1, friend = popular_kid)
                friendship.save()
            # if the student is the popular kid, then add some random guy
            else:

            # add a random dude (cannot be himself)
            if()
    
if __name__ =='__main__':
    print('populating script!')
    add_friendship()
    print("Populating complete!")