from django.db import models
from django.contrib.auth.models import User #유저 모델 import
from django.db.models.deletion import CASCADE

# Create your models here.
#modles.Model을 상속받는다.
class Write(models.Model): 
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=CASCADE)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Write, related_name="comments", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.post.title

# class User(models.Model):
#     job = models.TextField(max_length=100)
    # job=models.ForeignKey()


# 1. url로 간다
# 2. url에서 각각의 함수를 읽는다
# 3. 

    # models => forms


