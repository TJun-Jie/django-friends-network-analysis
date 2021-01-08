from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length =128)

    def __str__(self):
        return self.name

class Friendship(models.Model):
    friend1 = models.ForeignKey(Student,related_name="friend1",on_delete=models.CASCADE)
    friend2 = models.ForeignKey(Student,related_name="friend2",on_delete=models.CASCADE)
    friend3 = models.ForeignKey(Student,related_name="friend3",on_delete=models.CASCADE)