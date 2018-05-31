from django.contrib import admin
from post.filters import CreatedDateFilter
from post.forms import MyPostAdminForm
from post.models import Category, Post, Comment
from django.contrib.admin import AdminSite
from django.conf.urls import url
from django.template.response import TemplateResponse

class PostAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        post_urls = [
            url(r'^status/$', self.admin_site.admin_view(self.post_status_view))
        ]
        return post_urls + urls
    def post_status_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            posts=Post.objects.all(),
            key1=value1,
            key2=value2,
        )
        return TemplateResponse(request, "admin/post_status.html", context)
    form = MyPostAdminForm
    list_per_page = 10
    list_display = (
        'id', 'title', 'member',
        'is_deleted', 'created_at', )
    list_editable = ('is_deleted', )
    list_filter = (
        'member__permission',
        'category__name', 'is_deleted', )
    fieldsets = (
        ('기본정보', {
            'fields': (('member', 'category', ), )
        }),
        ('제목및내용', {
            'fields': (
                'title', 'subtitle', 'content',
            )
        }),
        ('삭제', {
            'fields': ('is_deleted', 'deleted_at', )
        })
    )
class CommentAdminSite(AdminSite):
    site_header = 'Comment administration'

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
#admin.site.register(Comment)

comment_admin = CommentAdminSite(name='comment admin')
comment_admin.register(Comment)
