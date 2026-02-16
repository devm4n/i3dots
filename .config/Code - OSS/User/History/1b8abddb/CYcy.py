from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    # user = User
    title = models.CharField()
    upload_on = models.DateTimeField()
    code = models.TextField()
    language = models.CharField()