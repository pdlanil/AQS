from django.db import models
from paragraph.models import Paragraph
# Create your models here.
class questions(models.Model):
    title=models.ForeignKey(Paragraph,on_delete=models.CASCADE)

    def __str__(self):
        return self.title