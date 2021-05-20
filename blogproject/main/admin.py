from django.contrib import admin
# 추가
from .models import Write, Comment


# Register your models here.
# admin 사이트에서 보기
admin.site.register(Write)
admin.site.register(Comment)