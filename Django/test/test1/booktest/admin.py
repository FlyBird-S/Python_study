from django.contrib import admin
from . import models
# Register your models here.
class HeroInfoInline(admin.TabularInline):
    model = models.Hero_Info
    extra = 2
class Book_admin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    inlines = [HeroInfoInline]

class Hero_admin(admin.ModelAdmin):
    list_display = ['id', 'hname','hcontent','hbook']
    list_filter = ['hbook']
admin.site.register(models.Book_Info,Book_admin)
admin.site.register(models.Hero_Info,Hero_admin)