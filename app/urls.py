# myapp/urls.py
from django.urls import path
from .views import LabelView, AnnotationView, LabelDeleteView

urlpatterns = [
    path('label/', LabelView.as_view(), name='label'),
    path('label/<int:pk>/', LabelDeleteView.as_view(), name='label_delete'),
    path('annotation/', AnnotationView.as_view(), name='annotation'),
    # Add more URL patterns as needed
]
