from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name='home-page'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.get_category,name='get_category'),
    url(r'^location/(\w+)', views.get_location,name='get_location'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  