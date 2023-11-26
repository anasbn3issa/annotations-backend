# annotation_service.py
from ..models import Annotation, Label

def create_annotation(label, start_position, end_position, annotated_text):
    return Annotation.objects.create(
        label=label,
        start_position=start_position,
        end_position=end_position,
        annotated_text=annotated_text
    )

def get_all_annotations():
    return Annotation.objects.all()
