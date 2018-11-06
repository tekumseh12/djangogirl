from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^kalkulacka/', views.kalkulacka, name= "kalkulacka"),
        url(r'^post/$', views.post, name="post"),
        url(r'^post/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
        url(r'^post/new/$', views.Formular, name = "new_post"),
        url(r'^kal_py/$', views.kal_py, name = "kal_py"),
            
    ]
