
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.success, name = "homepage"),
    path('studentform/', views.studentform, name='student_form'),
    path('teacherform/', views.teacher_form, name='TeacherForm'),
    path('login/', views.student_login, name ="login"),
    path('accounts/profile/', views.pdf_view, name = "mainpage"),
    path('aaa/', views.pdf_up, name = "pdf_upload_page"),
    path('teacher_login/', views.teacher_login_form, name ="teacher_login"),
    path('abc/', views.image_capture, name="image"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)