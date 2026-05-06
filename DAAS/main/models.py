from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User

class company(models.Model):
    name = models.CharField(max_length=100)
    inn = models.CharField(max_length=12, validators=[RegexValidator('[0-9]+')], unique=True)
    in_created = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
