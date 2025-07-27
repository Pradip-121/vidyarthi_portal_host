from django import forms
from .models import Assignment
from .models import Syllabus
from .models import UnitTestUpload
from .models import NewsEvent, ImportantLink
from .models import QuestionPaper

class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['class_name', 'year', 'semester', 'subject', 'theory_pdf', 'practical_pdf']

class SyllabusUploadForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['title', 'class_name', 'subject', 'year', 'file']

# class UnitTestUploadForm(forms.ModelForm):
#     class Meta:
#         model = UnitTestUpload
#         fields = ['class_name','year','semester','subject','theory_pdf','practical_pdf']


class NewsEventForm(forms.ModelForm):
    class Meta:
        model = NewsEvent
        fields = ['news_title', 'news_date', 'news_description', 'attachment']

class ImportantLinkForm(forms.ModelForm):
    class Meta:
        model = ImportantLink
        fields = ['link_title', 'link_url', 'link_description']

class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['class_name', 'exam', 'subject', 'upload_date', 'pdf_file']

class TeacherCreateTestForm(forms.ModelForm):
    class Meta:
        model = UnitTestUpload
        fields = ['class_name','year','semester','subject','theory_pdf','practical_pdf']