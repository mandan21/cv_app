from django.urls import path
from .views import register, upload_cv, view_cv

urlpatterns = [
    path('register/', register, name='register'),
    path('upload/', upload_cv, name='upload_cv'),
    path('cv/', view_cv, name='view_cv'),
]
