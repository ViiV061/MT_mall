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
