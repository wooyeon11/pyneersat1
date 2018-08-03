from django.contrib import admin
from .models import Post # 관리자 페이지에 포스트 모델을 가져온다

admin.site.register(Post)

# Register your models here.
