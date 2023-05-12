import re
from django.http import JsonResponse
from django.views import View
from apps.users.models import User


# Create your views here.
class UsernameCountView(View):

    def get(self, request, username):
        # 1. Get the username, check the validity of the username
        # if not re.match('[a-zA-Z0-9_-]{5,20}', username):
        #     return JsonResponse({'code': 200, 'errmsg': 'Username is invalid'})
        # 2. Query the database to see if the username exists
        count = User.objects.filter(username=username).count()
        # 3. Return the result

        return JsonResponse({'code': 0, 'errmsg': 'ok', 'count': count})


"""
user register
1. method  POST /register/
2. data: username, password, password2, mobile, sms_code, allow
3. check the validity of the data
4. check the validity of the sms code
5. create a user
6. return the result


"""

import json


class RegisterView(View):

    def post(self, request):
        # Receive the request json
        body_bytes = request.body
        body_str = body_bytes.decode()
        body_dict = json.loads(body_str)

        # get data
        username = body_dict.get('username')
        password = body_dict.get('password')
        password2 = body_dict.get('password2')
        mobile = body_dict.get('mobile')
        #email = body_dict.get('email')
        allow = body_dict.get('allow')

        # check the validity of the data
        if not all([username, password, password2, mobile, allow]):
            return JsonResponse({'code': 400, 'errmsg': 'data is not complete'})
        if not re.match('[a-zA-Z0-9_-]{5,20}', username):
            return JsonResponse({'code': 400, 'errmsg': 'username is invalid'})
        if not re.match('[a-zA-Z0-9]{8,20}', password):
            return JsonResponse({'code': 400, 'errmsg': 'password is invalid'})
        if password != password2:
            return JsonResponse({'code': 400, 'errmsg': 'password is not same'})
        if not re.match('^1[3-9]\d{9}$', mobile):
            return JsonResponse({'code': 400, 'errmsg': 'mobile is invalid'})
        # if not re.match('^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
        #     return JsonResponse({'code': 400, 'errmsg': 'email is invalid'})
        if allow != True:
            return JsonResponse({'code': 400, 'errmsg': 'allow is not True'})
        # check the validity of the sms code
        # create a user
        # user = User(username=username, password=password, mobile=mobile, email=email)
        # user.save()
        user = User.objects.create_user(username=username, password=password, mobile=mobile)  # email=email

        # login status check, use SessionMiddleware
        from django.contrib.auth import login
        login(request, user)

        # return the result
        return JsonResponse({'code': 0, 'errmsg': 'ok'})

