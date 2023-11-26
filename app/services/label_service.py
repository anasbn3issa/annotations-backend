# label_service.py
from ..models import Label

def create_label(name, color):
    try:
        label = Label.objects.create(name=name, color=color)
        return {'status': 'created', 'label_id': label.id}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def get_all_labels():
    return Label.objects.all()

