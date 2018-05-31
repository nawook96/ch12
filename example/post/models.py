from django.db import models
from member.models import Member

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=20)

class Post(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='카테고리', on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=255)
    content = models.TextField('내용')
    is_deleted = models.BooleanField('삭제된 글', default=False)
    created_at = models.DateTimeField('작성일', auto_now_add=True)

class Comment(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='원본글', on_delete=models.CASCADE)
    content = models.TextField()
    is_blocked = models.BooleanField('노출 제한', default=False)
