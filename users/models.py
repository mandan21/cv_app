from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='cvs/')
    data = models.JSONField()  # Store Excel contents as JSON
    uploaded_at = models.DateTimeField(auto_now_add=True)