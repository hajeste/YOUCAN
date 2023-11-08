from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    consent = models.BooleanField(default=False)
    submission_time = models.DateTimeField(auto_now_add=True)
