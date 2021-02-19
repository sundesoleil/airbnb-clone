from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ Custom User Model """

    GENDER_FEMALE = "female"
    GENDER_MALE = "male"
    GENDER_OTHRE = "other"

    GENDER_CHOICES = (
        (GENDER_FEMALE, "Female"),
        (GENDER_MALE, "Male"),
        (GENDER_OTHRE, "Other"),
    )

    LANGUAGE_KOREAN = "kr"
    LANGUAGE_ENGLSIH = "en"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_ENGLSIH, "English"),
    )

    CURRENCY_KRW = "krw"
    CURRENCY_USD = "usd"

    CURRENCY_CHOICES = (
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_USD, "USD"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
