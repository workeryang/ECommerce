from django.http import JsonResponse
import json
import uuid
import traceback

from ECommerce.apps.user.models import UserInfo, Role
from ECommerce.libs.decorations import login_required


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

                data['meta']['msg'] = 'hava not this username {},login flaid.'.format(
                    username)

                return JsonResponse(data, status=400)

            if obj.password != pwd:

                data['meta']['msg'] = 'password error,login flaid.'

                return JsonResponse(data, status=400)
        except:

            data['meta']['msg'] = 'hava not this username {},login flaid.'.format(
                username)

            return JsonResponse(data, status=400)

        token = uuid.uuid4()

        data['meta']['status'] = 200
        data['meta']['msg'] = 'login success'
        data['data']['token'] = token
        data['data']['user'] = obj.to_dict()

        return JsonResponse(data, status=200)

    data['meta']['msg'] = 'bad request'
    return JsonResponse(data, status=400)


@login_required
def users(request):
    """users data api"""

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
            "role_name": item.roles.all()[0].role_name if item.roles.all() else ''
        } for item in user_list]

        return JsonResponse(data=data, status=200)

    elif request.method == 'POST':

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
            data['meta']['msg'] = 'username {} already be used.'.format(
                req_data.get('username'))
            return JsonResponse(data, status=400)

        try:
            obj = UserInfo.objects.create(**req_data)
        except:
            data['meta']['msg'] = 'invalid params,create fail.'
            return JsonResponse(data, status=400)

        data['meta']['msg'] = 'create success.'
        data['meta']['status'] = 200
        data['data']['user'] = obj.to_dict()
        return JsonResponse(data, status=200)

    data['meta']['msg'] = 'bad request'
    data['meta']['status'] = 400
    return JsonResponse(data, status=400)


@login_required
def user(request, uid):

    data = {
        'data': {
            'user': '',
        },
        'meta': {
            'status': 400,
            'msg': ''
        }
    }

    try:
        obj = UserInfo.objects.filter(id=int(uid)).first()
        if not obj:
            data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
            return JsonResponse(data, status=400)
    except:
        data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
        return JsonResponse(data, status=400)

    if request.method == 'GET':

        data['data']['user'] = obj.to_dict()
        data['meta']['msg'] = 'success'
        data['meta']['status'] = 200
        return JsonResponse(data, status=200)
    elif request.method == 'PUT':
        try:
            req_data = json.loads(request.body.decode('utf-8'))
            obj.email = req_data.get('email')
            obj.mobile = req_data.get('mobile')
            obj.save()

            data['data']['user'] = obj.to_dict()
            data['meta']['msg'] = 'update success'
            data['meta']['status'] = 200
        except:
            traceback.print_exc()
            data['meta']['msg'] = 'update fiald'
            return JsonResponse(data, status=400)
        return JsonResponse(data, status=200)
    elif request.method == 'DELETE':
        data = {
            'data': '',
            'meta': {
                'status': 400,
                'msg': ''
            }
        }
        obj.delete()
        data['meta']['status'] = 200
        data['meta']['msg'] = 'delete success'
        return JsonResponse(data, status=200)


@login_required
def user_state(request, uid, state):

    data = {
        'data': {
            'user': '',
        },
        'meta': {
            'status': 400,
            'msg': ''
        }
    }
    try:
        obj = UserInfo.objects.filter(id=int(uid)).first()
        if not obj:
            data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
            return JsonResponse(data, status=400)
    except:
        data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
        return JsonResponse(data, status=400)

    if request.method == 'PUT':

        obj.state = int(state)
        obj.save()

        data['data']['user'] = obj.to_dict()
        data['meta']['msg'] = 'success'
        data['meta']['status'] = 200
        return JsonResponse(data, status=200)


@login_required
def user_role(request, uid):
    """给用户分配单个角色"""

    data = {
        'data': "",
        'meta': {
            'status': 400,
            'msg': ''
        }
    }

    # 检查看有没有与id对应的数据
    try:
        u_obj = UserInfo.objects.get(id=int(uid))
    except UserInfo.DoesNotExist:
        data['meta']['msg'] = 'the user id={} do not exist.'.format(uid)
        return JsonResponse(data, status=400)
    try:
        req_data = json.loads(request.body.decode('utf-8'))
        rid = int(req_data.get('rid'))
        r_obj = Role.objects.get(id=rid)
    except Role.DoesNotExist:
        data['meta']['msg'] = 'the role id={} do not exist.'.format(rid)
        return JsonResponse(data, status=400)

    # 有数据 则更新数据
    try:
        # 多对多 增加操作
        u_obj.roles.add(r_obj)
    except:
        traceback.print_exc()
        data['meta']['msg'] = 'fail'
        return JsonResponse(data, status=400)
        
    data['meta']['status'] = 200
    data['meta']['msg'] = 'success'
    return JsonResponse(data, status=200)