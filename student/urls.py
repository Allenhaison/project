from django.contrib import admin
from django.urls import path
from main import views  # Replace 'main' with your app name if different
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_profile, name='student_profile'),  # Root URL for the student profile form
    path('view/', views.view_students, name='view_students'), 
     path('students/delete/<str:student_id>/', views.delete_student, name='delete_student'),
    path('students/edit/<str:student_id>/', views.edit_student, name='edit_student'),
     path('', views.index, name='index'),
     path('view_student/<str:student_id>/', views.view_student_details, name='view_student_details'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
