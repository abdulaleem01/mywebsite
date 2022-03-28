from email import message
from django.db import models

# Create your models here.
   
# declare a new model with a name "GeeksModel"
class ContactsModel(models.Model):
        # fields of the model
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=500)
    
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.name