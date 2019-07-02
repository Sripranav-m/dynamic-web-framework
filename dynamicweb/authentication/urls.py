from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()

from . import views

urlpatterns = [
    path('',views.form_to_login,name='loginform'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.login,name='login'),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                              