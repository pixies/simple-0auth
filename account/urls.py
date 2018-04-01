from django.conf.urls import url, include
from django.contrib.auth import views

from account.views import home, update_profile

urlpatterns = [
    url(r'^home/', home, name='home'),
    url('^profile/', update_profile),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

]
