# myapp/urls.py
from django.urls import path
from .views import LabelView, AnnotationView, LabelDeleteView, clear_database, clear_annotations

urlpatterns = [
    path('label/', LabelView.as_view(), name='label'),
    path('label/<int:pk>/', LabelDeleteView.as_view(), name='label_delete'),
    path('annotation/', AnnotationView.as_view(), name='annotation'),
    path('clear-database/', clear_database, name='clear_database'),
    path('clear-annotations/', clear_annotations, name='clear_annotations'),
    # Add more URL patterns as needed
]
