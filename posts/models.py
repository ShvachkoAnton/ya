from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.db.models.fields import related
User=get_user_model()
class Post(models.Model):
    text=models.CharField(max_length=25,null=True,verbose_name='введите текст' )
    pub_date=models.DateTimeField('date published',auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='posts')
# Create your models here.
    def __str__(self):
        return self.text

   

class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)