from django.contrib import admin

from .models import SiteUser, ReqruitmentObj, ActionObj

admin.site.register(SiteUser)
admin.site.register(ReqruitmentObj)
admin.site.register(ActionObj)
