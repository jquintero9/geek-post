
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^', include('articulo.urls', namespace='articulo')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
]


