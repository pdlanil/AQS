from django.db import models

# Create your models here.


class Paragraph(models.Model):
    title=models.TextField(max_length=100,default='please give title',null=False,blank=False)
    description=models.TextField(max_length=20000,null=False,blank=False)

    def __str__(self):
        return self.title



