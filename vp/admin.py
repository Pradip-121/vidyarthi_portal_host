# vp/admin.py
from django.contrib import admin
from .models import Assignment , Syllabus , UnitTestUpload
from .models import NewsEvent, ImportantLink
from .models import QuestionPaper

admin.site.register(Assignment)
admin.site.register(Syllabus)
admin.site.register(UnitTestUpload)
admin.site.register(NewsEvent)
admin.site.register(ImportantLink)
admin.site.register(QuestionPaper)
