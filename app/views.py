from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Label, Annotation


@method_decorator(csrf_exempt, name='dispatch')
class LabelView(View):
    def get(self, request):
        my_models = list(Label.objects.values())
        return JsonResponse(my_models, safe=False)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('name', '')
        color = data.get('color', '')
        Label.objects.create(name=name, color=color)
        return JsonResponse({'status': 'created'}, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AnnotationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            start_position = data.get('start_position', 0)
            end_position = data.get('end_position', 0)
            label = data.get('label', '')
            annotated_text = data.get('annotated_text', '')

            annotation = Annotation.objects.create(
                start_position=start_position,
                end_position=end_position,
                label=label,
                annotated_text=annotated_text
            )

            return JsonResponse({'status': 'created', 'annotation_id': annotation.id}, status=201)
        except Exception as e:
            print(f"Error in post method: {e}")
            return JsonResponse({'status': 'error'}, status=500)

    def get(self, request):
        annotations = list(Annotation.objects.values())
        return JsonResponse(annotations, safe=False)
