from django.db import models

class Registration(models.Model):
    full_name=models.CharField(max_length=40,null=0,default=0)
    dob=models.DateField(max_length=20,default=0)
    email=models.EmailField(max_length=10)
    password=models.CharField(max_length=50,null=0,default=0)
    cpassword=models.CharField(max_length=50,null=0,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
