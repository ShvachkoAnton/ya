from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
class Post(models.Model):
    text=models.CharField(max_length=25,verbose_name='введите текст' )
    pub_date=models.DateTimeField('date published',auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
# Create your models here.
    def __str__(self):
        return self.text
