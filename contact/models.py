from django.db import models


class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.full_name