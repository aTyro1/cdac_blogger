from django.db import models
from datetime import date
from jsonfield import JSONField

class writer(models.Model):
    writer_name=models.CharField(max_length=30,null=False)
    writer_id=models.CharField(max_length=30,null=False,default='')

class verified_writer(models.Model):
    writer_name=models.CharField(max_length=30,null=False)
    writer_id=models.CharField(max_length=30,null=False,default='',primary_key=True)

class blogs(models.Model):
    date=models.DateField(default=date.today())
    title=models.CharField(max_length=200,null=False,default='Title of the Article!<GENERATED by SYSTEM>')
    blog=models.TextField(default='')
    writer_id=models.CharField(max_length=200,null=False,default='')
    writer_name=models.CharField(max_length=200,null=False,default='')
    comments=JSONField(JSONField())


