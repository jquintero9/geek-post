from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Email(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=250)

try:
    email = Email.objects.get(id=1)
    print 'email: ', email.email
    print 'password: ', email.password
    settings.EMAIL_HOST_USER = email.email
    settings.EMAIL_HOST_PASSWORD = email.password
except Exception:
    pass


