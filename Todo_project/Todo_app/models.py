from django.db import models
from django.contrib.auth.models import User
# Create your models here.
H="High"
L="Low"
A="Avarage"
c="Completed"
w="Work in Progress"
n="Not Started"
crik=[(H,"High"),(L,"Low"),(A,"Avarage")]
stat=[(c,"Completed"),(w,"Work in Progress"),(n,"Not Started")]

class work(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    created_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    criticality=models.CharField(max_length=100,choices=crik)
    status=models.CharField(max_length=100,choices=stat)
    user=models.ForeignKey(User,on_delete="CASCADE")


    def __str__(self):
        return self.title

class todo_work(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    created_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    criticality=models.CharField(max_length=100,choices=crik)
    status=models.CharField(max_length=100,choices=stat)
    user=models.ForeignKey(User,on_delete="CASCADE")


    def __str__(self):
        return self.title
