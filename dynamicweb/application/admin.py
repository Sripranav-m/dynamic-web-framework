from django.contrib import admin
from .models import Formdata,Menu,carousel_Image,content_for_Menu

admin.site.register(Formdata)
admin.site.register(Menu)
admin.site.register(carousel_Image)
admin.site.register(content_for_Menu)


admin.site.site_header = "IT CRATS -> ADMIN-PANEL"
admin.site.index_title = "USER DATA"