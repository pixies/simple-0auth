from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls', namespace='account')),
    #url(r'^account/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^account/', include('social_django.urls', namespace='social')),  # <- Here
#
]
