from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='Home'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('start_scan', views.start_scan, name='start_scan'),
    path('stop_scan', views.stop_scan, name='stop_scan'),
    path('scan/', views.scan, name='scan'),
]