from django.db import models

# 데이터베이스와 연결되는 python의 class

class Post(models.Model):
    title = models.CharField(max_length=64)
    user = models.CharField(max_length=32)
    # user는 실제 프로젝트 개발시 CharField X
    content = models.TextField()
    region = models.CharField(max_length=16)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)