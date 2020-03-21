
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('googleapi/', include('social_django.urls', namespace ='social')),

    path('admin/', admin.site.urls),
    path('',include('student_registration_form.urls')),
    
]
