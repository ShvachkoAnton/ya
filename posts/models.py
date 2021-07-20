from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.db.models.fields import related
User=get_user_model()


class Post(models.Model):
    text=models.CharField(max_length=25,null=True,verbose_name='введите текст' )
    pub_date=models.DateTimeField('date published',auto_now_add=True,)  #db_index=True для оптимизации#
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='posts')
    image=models.ImageField(upload_to='posts/',blank=True,null=True)
   
# Create your models here.
    def __str__(self):
        return self.text


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text






class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',related_name='rel_from_set',
    on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
    related_name='rel_to_set',
    on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
    db_index=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
user_model = get_user_model()
user_model.add_to_class('following',
 models.ManyToManyField('self',
 through=Contact,
 related_name='followers',
 symmetrical=False))