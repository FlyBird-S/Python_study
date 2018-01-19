from django.contrib import admin
from . import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','pub_time')
    list_filter = ('pub_time',)
    # def __init__(self):
    #     self.list_display = ('title','content')
admin.site.register(models.Article,ArticleAdmin)