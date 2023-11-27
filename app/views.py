from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404
from django.core.management import call_command




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
        label = Label.objects.create(
            name = name,
        )
        return JsonResponse({'status': 'created', 'name': label.id}, status=201)
    
@method_decorator(csrf_exempt, name='dispatch')
class LabelDeleteView(View):
    def delete(self, request, pk):
        label = get_object_or_404(Label, pk=pk)
        label.delete()
        return JsonResponse({'status': 'deleted'}, status=204)


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


@csrf_exempt
def clear_database(request):
    if request.method == 'POST':
        call_command('clear_db')
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def clear_annotations(request):
    if request.method == 'POST':
        call_command('clear_annotations')
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
