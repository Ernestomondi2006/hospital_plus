from django.db import models

# Create your models here.
class appointment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    date = models.DateTimeField()
    department = models.CharField(max_length=150)
    doctor = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name









class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name