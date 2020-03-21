from django.contrib import admin

from .models import pdf_file,TeachersInfo


admin.site.register(pdf_file),
admin.site.register(TeachersInfo)