# Markdown語法測試>>>我的django練習部落格
## 以詩人為範例
### 創建專案
1. 建立新資料夾，點擊內部並同時按下shift+滑鼠右鍵，選擇Powershwell 視窗
2. 打入以下指令
```
django-admin startproject myblog  # myblog為自訂創建資料夾名字，可修改
python manage.py startapp mainsite
python manage.py runserver
```
3. 基本架構
- manage.py   管理納站組態，所有命令都是執行此程式，平常不會修改
- myblog 與專案同名，放專案設定檔
- urls.py 對應每個網址要對應的函數及方式，建新網頁先編輯
- wsgi.py 和其它伺服器溝通的介面
- settings.py 網站系統設計的所在位置，建新網站先編輯
- 先把剛建立的mainsite APP加進去，用startapp mainsite建立app來運作

4. 設定settings.py
```
INSTALLED_APPS = [
    原先程式碼
    'mainsite', # 加入此app
]

LANGUAGE_CODE = 'zh-Hant'  # 修改語言
TIME_ZONE = 'Asia/Taipei'  # 修改地區
```
5. 設定資料庫
- 輸入python manage.py migrate ，把現在程式資料，轉換成真的資料庫

6. 建立資料表進入資料庫
- 轉換到models.py內，新增的資料表
```
class Post(models.Model):
    title = models.CharField(max_length=200) 
    slug = models.CharField(max_length=200)  
    abstract = models.CharField(max_length=200)  
    pic_url= models.URLField(max_length=250)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)  
    class Meta:  
        ordering = ('-pub_date',) 
    def __str__(self):
        return self.title  
```
- 再輸入python manage.py makemigrations，把物件建立好，變成寫入資料庫的文件檔
- 再輸入python manage.py migrate 寫入資料庫

7. 建立管理員
- python manage.py createsuperuser
- 進入http://127.0.0.1:8000/admin/  登入
- 開啟admin.py，加入admin.site.register(Post,PostAdmin)

8. 增加post內容
```
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')
```
9. 網頁顯示資料庫內容
- 進入views.py
```
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) +str(post)+"<br>")
        post_lists.append(str(post.pub_date)+"<br>")
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    return HttpResponse(post_lists)
```
- 在urls.py，增加連結
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
]
```

### 美化網頁
1. 在setting.py增加模板
```
TEMPLATES = [
    {原本程式碼,
    'DIRS': [os.path.join(BASE_DIR, 'templates')], # 增加網頁模板連結
    原本程式碼
    },},]
```

2. 在views.py加入回傳的模組，並且建立index.html
```
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
```

3. urls.py增加showpost模組，並在urlpatterns加上path('post/<slug:slug>/', showpost),

4. 在views.py建立showpost函數，並建立post.html當作分頁
```
def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
```

5. 加入本地端圖片
- 建立static資料夾，並在settings.py加入連結
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
```

## 加入Markdown語法
1. 在setting.py加入markdown_deux
```
INSTALLED_APPS = [
    原本程式碼
    'markdown_deux',
    原本程式碼
]
```

2. markdown可以使用html
- 在setting.py修改
```
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}
```