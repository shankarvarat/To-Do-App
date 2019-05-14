from django.db import models

# Create your models here.
class todo(models.Model):
    work=models.TextField(max_length=300)
    created_at=models.DateField()
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.work