from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # extra information
    class Meta:
        abstract = True  # DB에 등록되지 않게 하기 위한 추상 모델
