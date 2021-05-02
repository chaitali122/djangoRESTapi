from django.db import models

# Create your models here.
class Movie(models.Model):
    id =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    director =models.CharField(max_length=60)
    genre =models.CharField(max_length=60)
    rating =models.IntegerField()
    release_date =models.DateField()

    def __str__(self):
        return self.name
