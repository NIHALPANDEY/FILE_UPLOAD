from django.db import models
from django.contrib.auth.models import User
from .utils import file_extension_validator
# Create your models here.

class Attachment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=50, null=True, blank=True)
    document = models.FileField(upload_to="documents/", max_length=1280, blank=True, null=True, validators=[file_extension_validator])

    def __str__(self):
        return self.filename
