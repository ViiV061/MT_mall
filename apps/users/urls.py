from django.urls import path, re_path
from apps.users.views import UsernameCountView, RegisterView

urlpatterns = [
    # Determine if the username is duplicated
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
    path('register/', RegisterView.as_view(),)
]
