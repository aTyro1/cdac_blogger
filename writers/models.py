from django.db import models

class writer(models.Model):
    first_name=models.CharField(max_length=30,null=False)
    password=models.CharField(max_length=10,null=False,default='cdac123')
    email=models.EmailField(max_length=25,null=False,default='')
    writer_id=models.CharField(max_length=30,null=False,default='')