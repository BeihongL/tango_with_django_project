from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),  # 这里引号里面的空代表的就是http://...rango/这个链接直接就是主页的样子
    path('about/', views.about, name='about'),  # 这里记得about后面价格斜杠，不然无法匹配对应的链接，因为rango/后的地址是交由这个urls文件处理的，后面出现的要打齐
]
