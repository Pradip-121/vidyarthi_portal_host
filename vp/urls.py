from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # Custom login and dashboard
    path('login/', views.custom_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Upload pages
    path('upload-assignment/', views.upload_assignment, name='upload_assignment'),
    path('upload_news_links/', views.upload_news_links, name='upload_news_links'),
    path('upload_question_paper/', views.upload_question_paper, name='upload_question_paper'),
    path('upload_syllabus/', views.upload_syllabus, name='upload_syllabus'),
    path('upload_unit_test/', views.upload_unit_test, name='upload_unit_test'),
    path('create_unit_test/', views.teacher_create_test, name='teacher_create_test'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),

    # Student facing pages
    path('course/', views.course, name='course'),
    path('home_assignments/', views.home_assignments, name='home_assignments'),
    path('news_events/', views.news_events, name='news_events'),
    path('practicals/', views.practicals, name='practicals'),
    path('question_papers/', views.question_papers, name='question_papers'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('unit_tests/', views.unit_tests, name='unit_tests'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
