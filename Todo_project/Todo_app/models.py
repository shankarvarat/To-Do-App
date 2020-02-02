from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
H="High"
L="Low"
A="Avarage"
c="Completed"
w="Work in Progress"
n="Not Started"
crik=[(H,"High"),(L,"Low"),(A,"Avarage")]
stat=[(c,"Completed"),(w,"Work in Progress"),(n,"Not Started")]



    

class works(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    created_date=models.DateField(default=datetime.now, blank=True)
    due_date=models.DateField(default=datetime.now, blank=True)
    criticality=models.CharField(max_length=100,choices=crik)
    status=models.CharField(max_length=100,choices=stat)
    user=models.ForeignKey(User,on_delete="CASCADE",null=True)


    def __str__(self):
        return self.title
