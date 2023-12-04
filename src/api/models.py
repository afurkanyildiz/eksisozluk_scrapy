from django.db import models


class eksisozluk_entries(models.Model):
    _id = models.AutoField(primary_key=True)
    titleId = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    author_profile_link = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    entryId = models.CharField(max_length=250)
    content = models.TextField()
    entry_date = models.DateTimeField()
    entry_date_from_scape = models.DateTimeField()
