from django.db import models

class Batch(models.Model):
    batchid = models.CharField(max_length=70)
    studentid = models.CharField(max_length=70)