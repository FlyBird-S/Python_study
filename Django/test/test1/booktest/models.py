from django.db import models

# Create your models here.
class Book_Info(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.btitle
class Hero_Info(models.Model):
    hname = models.CharField(max_length=10)
    hgander = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(Book_Info,on_delete=models.CASCADE,) #2.0 写法
    def __str__(self):
        return self.hname

