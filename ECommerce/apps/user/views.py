from django.http import JsonResponse
import json
import uuid

from ECommerce.apps.user.models import UserInfo


def login(request):
    """login api"""
    
    if request.method == 'POST':
        req_data = json.loads(request.body.decode('utf-8'))
        username = req_data.get('username')
        pwd = req_data.get('password')

        data = {
                'data': {
                    'user': '',
                    'token': '',
                },
                'meta': {
                    'status': 400,
                    'msg': ''
                }
            }

        try:
            obj = UserInfo.objects.filter(username=username).first()
            if not obj:

                data['meta']['msg'] = 'hava not this username {},login flaid.'.format(username)

                return JsonResponse(data, status=400)     
            
            if obj.password != pwd:

                data['meta']['msg'] = 'password error,login flaid.'

                return JsonResponse(data, status=400)  
        except:

            data['meta']['msg'] = 'hava not this username {},login flaid.'.format(username)

            return JsonResponse(data, status=400)   

        token = uuid.uuid4()

        data['meta']['status'] = 200
        data['meta']['msg'] = 'login success'
        data['data']['token'] = token
        data['data']['user'] = obj.to_dict()

        return JsonResponse(data, status=200)

    data['meta']['msg'] = 'bad request'
    return JsonResponse(data, status=400)  

def users(request):
    """users data api"""

    # check token here
    if not request.META.get('HTTP_AUTHORIZATION'):
        data = {
            "data": '',
            "meta": {
                "msg": "you has no auth, please login first.",
                "status": 400
            }
        }
        return JsonResponse(data, status=400)

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
            "is_super": item.is_super,
            "email": item.email,
            "create_time": item.create_time,
            "update_time": item.update_time,
            "state": item.state,
            "role_name": item.users.all()[0].role_name if item.users.all() else ''
        } for item in user_list]

        return JsonResponse(data=data, status=200)

    if request.method == 'POST': 
        
        data = {
                'data': {
                    'user': '',
                },
                'meta': {
                    'status': 400,
                    'msg': ''
                }
            }

        req_data = json.loads(request.body.decode('utf-8'))

        # check username
        if UserInfo.objects.filter(username=req_data.get('username')).exists():
            data['meta']['msg'] = 'username {} already be used.'.format(req_data.get('username'))
            return JsonResponse(data, status=400)

        try:
            obj = UserInfo.objects.create(**req_data)
        except:
            data['meta']['msg'] = 'invalid params,create faild.'
            return JsonResponse(data, status=400)

        data['meta']['msg'] = 'create success.'
        data['meta']['status'] = 200
        data['data']['user'] = obj.to_dict()
        return JsonResponse(data, status=200) 

    data['meta']['msg'] = 'bad request'
    data['meta']['status'] = 400
    return JsonResponse(data, status=400)  

def user_operate(request, uid):
    """user oprerate:update,get,delete"""

    if request.method == 'GET':
        data = {
            "data": {
                "user": ''
            },
            "meta": {
                "msg": "",
                "status": 400
            }
        }
        print(type(uid))
        try:
            obj = UserInfo.objects.filter(id=int(uid)).first()
            if not obj:
                data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
                return JsonResponse(data, status=400)
        except:
            data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
            return JsonResponse(data, status=400)
        
        data['data']['user'] = obj.to_dict()
        data['meta']['msg'] = 'success'
        data['meta']['status'] = 200
        return JsonResponse(data, status=200)