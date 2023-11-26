# myapp/urls.py
from django.urls import path
from .views import LabelView, AnnotationView

urlpatterns = [
    path('label/', LabelView.as_view(), name='label'),
    path('annotation', AnnotationView.as_view(), name='annotation')
    # Add more URL patterns as needed
]
