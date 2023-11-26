from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Annotation(models.Model):
    label = models.CharField(max_length=255)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    annotated_text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label.name} - {self.annotated_text}"
