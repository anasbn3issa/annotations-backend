from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=7)  # Assuming hexadecimal color code, e.g., "#RRGGBB"

    def __str__(self):
        return self.name

class Annotation(models.Model):
    document = models.TextField()  # Assuming you store the annotated document as text
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
    annotated_text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label.name} - {self.annotated_text}"
