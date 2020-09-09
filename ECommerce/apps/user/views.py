from django.http import JsonResponse


def login(request):
    print(request.body)
    return JsonResponse({'status': 200})
