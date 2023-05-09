from django.urls import converters


class UsernameConverter:
    # Define a regex to match the username
    regex = '[a-zA-Z0-9_-]{5,20}'

    # Define a method to match the username
    def to_python(self, value):
        return value

