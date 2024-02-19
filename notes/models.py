from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='notes',default=1)
    # updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
