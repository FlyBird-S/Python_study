from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now=True)
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(null=False, db_column='comment_count')
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table='bookinfo'
    def __str__(self):
        return self.btitle
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgander = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def showname(self):
        return self.hname
    def __str__(self):
        return self.hname