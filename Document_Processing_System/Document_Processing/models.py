from django.db import models
from django import forms 

class User(models.Model):
    email = models.EmailField() 
    phone_no = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20) 
    last_name = models.CharField(max_length = 20)  
    
    def __str__(self):
        return self.email
    
class Document(models.Model): 
    Title = models.CharField(max_length=50)
    Upload_Document = models.FileField()

    

  