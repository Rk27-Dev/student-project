from django.contrib import admin

# Register your models here.
from app.models import sms,sms_login
admin.site.register(sms)
admin.site.register(sms_login)