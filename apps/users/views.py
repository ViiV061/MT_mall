from django.http import JsonResponse
from django.views import View

from apps.users.models import User


# Create your views here.
class UsernameCountView(View):

    def get(self, request, username):
        # 1. Get the username
        # 2. Query the database to see if the username exists
        count = User.objects.filter(username=username).count()
        # 3. Return the result

        return JsonResponse({'code': 0, 'errmsg': 'ok', 'count': count})
