from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)


class Content(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="contents")
    text = RichTextUploadingField(blank=True, null=True)
    file = models.FileField(upload_to="documents")
