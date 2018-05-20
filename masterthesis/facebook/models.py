from django.db import models

class PostFeatures (models.Model):
    number_of_words = models.IntegerField(null=False)
