from django.db import models


# Create your models here.
class BookinfoManager(models.Manager):  # 自定义管理器
    def get_queryset(self):
        return super(BookinfoManager, self).get_queryset().filter(isDelete=False)
    def create(self,title,pub_date):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = pub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete =False
        return b
'''
b = BookInfo.books2.create('abc',datetime(2019,1,2))
b.save()
'''

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now=True)
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False, db_column='comment_count')
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'

    books1 = models.Manager()  # 重设管理器 代替 xx.objects.xx
    books2 = BookinfoManager()
    @classmethod
    def create(cls,title,pub_date):   # 定义一个类创建方法， 因为__init__被父对象使用。
        b = BookInfo()
        b.btitle = title
        b.bpub_date = pub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete =False
        return b
    def __str__(self):
        return self.btitle
'''
b = BookInfo.create('abc',datetime(2019,1,2))
b.save()
'''
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgander = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.hname
