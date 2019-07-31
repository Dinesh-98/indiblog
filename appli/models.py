from django.db import models

# Create your models here.
class AppModel(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)

    def __str__(self):
        return self.name
