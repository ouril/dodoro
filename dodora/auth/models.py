import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

from dodora.api.models import Company


class User(AbstractUser):
    CHOICE = (
        ('EM', 'Employer'),
        ('AD', 'Administrator'),
        ('OW', 'Owner')
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    company = models.ForeignKey(
        Company,
        verbose_name='API user',
        related_name="api_user",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    position = models.CharField(choices=CHOICE, verbose_name='position', max_length=2, default='EM')

def __str__(self):
    return self.username
