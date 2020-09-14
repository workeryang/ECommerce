from django.shortcuts import render
from ECommerce.apps.web.models import Right
from django.http import JsonResponse


def right(request, data_type):
    """权限"""

    if request.method == 'GET':

        if data_type == 'list':
            data = {
                'data': {
                    'rights': []
                },
                'meta': {
                    'status': 400,
                    'msg': ''
                }
            }
            right_list = Right.objects.all()
            data['data']['rights'] = [item.to_dict() for item in right_list]
            data['meta']['status'] = 200
            data['meta']['msg'] = 'get rights success'

            return JsonResponse(data, status=200)
        elif data_type == 'tree':

            right_list = Right.objects.all()
            menu_list = []
            item = {
                'id': None,
                'auth_name': None,
                'level': None,
                'path': None,
                'parent': None,
                'children': []
            }




            return JsonResponse({'msg': 'ok'}, status=200)

    return JsonResponse({'msg': 'ok'}, status=200)
