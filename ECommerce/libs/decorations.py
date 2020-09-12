import functools
from django.http import JsonResponse


def login_required(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if not args[0].META.get('HTTP_AUTHORIZATION'):
            data = {
                "data": '',
                        "meta": {
                            "msg": "you has no auth, please login first.",
                            "status": 400
                        }
            }
            return JsonResponse(data, status=400)

        return func(*args, **kwargs)

    return wrapper
