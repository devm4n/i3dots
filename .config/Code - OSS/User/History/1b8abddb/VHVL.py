from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    # user = User
    title = models.CharField()
    upload_on = models.DateTimeField(auto_now=True)
    code = models.TextField()
    language = models.CharField()