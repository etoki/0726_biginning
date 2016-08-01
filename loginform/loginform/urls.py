from django.conf.urls import *
from app.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', registration),
    url(r'^login/', login),
    url(r'^forgot/', forgot),
]
