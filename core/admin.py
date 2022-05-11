from django.contrib import admin

# Register your models here.
from core.models import Content, Video, HtmlContent

admin.site.register(Content)
admin.site.register(Video)
admin.site.register(HtmlContent)
