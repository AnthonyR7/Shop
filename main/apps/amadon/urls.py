from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process),
    url(r'^final_sale$', views.final_sale),
    url(r'^back$', views.goback)
  ]
