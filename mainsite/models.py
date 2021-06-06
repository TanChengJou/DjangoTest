from django.db import models
from django.utils import timezone
# Create your models here. 注意縮排

# 新增的資料表
class Post(models.Model):
    title = models.CharField(max_length=200) #charfield字串
    slug = models.CharField(max_length=200)  # 子網址
    abstract = models.CharField(max_length=200)  
    pic_url= models.URLField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)  # 發布日期 timezone現在時間
    
    # 預設發布日期
    class Meta:  
        ordering = ('-pub_date',) # 減字號代表倒續


    def __str__(self):
        return self.title  # 會顯示title

