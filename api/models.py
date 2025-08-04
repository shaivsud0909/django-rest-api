from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established_date = models.DateField()
    def __str__(self):
        return self.name
 

class Worker(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=200)    
    Company=models.ForeignKey(Company,on_delete=models.CASCADE)

    
