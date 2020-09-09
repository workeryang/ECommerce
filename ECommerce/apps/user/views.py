from django.http import JsonResponse

from ECommerce.apps.user.models import UserInfo


def login(request):
    print(request.body)
    return JsonResponse({'status': 200})


def users(request):
    # get all user info
    if request.method == 'GET':
        data = {
            "data": {
                "total": 5,
                "pagenum": 1,
                "users": []
            },
            "meta": {
                "msg": "get data success",
                "status": 200
            }
        }
        user_list = UserInfo.objects.all()

        data['data']['users'] = [{
            "id": item.id,
            "username": item.username,
            "mobile": item.mobile,
            "type": item.type,
            "email": item.email,
            "create_time": item.create_time,
            "update_time": item.update_time,
            "state": item.state,
            "role_name": 'op'
        } for item in user_list]

        return JsonResponse(data=data, status=200)

    return JsonResponse({'status': 200})
