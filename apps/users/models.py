from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     email = models.EmailField(max_length=50, unique=True)


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = 'Users'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
