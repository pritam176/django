from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.encoding import smart_str


class CatalogueRegister(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.CharField(max_length=13)
    WhatsappNo = models.CharField(max_length=13)
    EmailD = models.CharField(max_length=50)
    Desc = models.TextField()
    CreatedDate = models.DateTimeField(default=timezone.now)
    list_display = ("Name", "Number", "EmailD")


class Meta:
        ordering = ("CreatedDate")


def __str__(self):
        return smart_str('foo: %s' % self.name)

