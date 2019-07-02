from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
admin.autodiscover()

from . import views

urlpatterns = [
    path('form/',views.createform, name='createform'),
    path('createmenu/',views.createmenu,name="createmenu"),
    path('content/<str:name>/',views.contentformenuview,name="contentformenu"),
    path('carousel/',views.addcarousel,name="carousel"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                              