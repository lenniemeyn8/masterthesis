from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^setFeatures/$', views.setFeatures, name='setFeatures'),
]