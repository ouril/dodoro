import uuid

from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

from api.models import Company


class AdminUser(User):
    CHOICE = (
        ('EM', 'Employer'),
        ('AD', 'Administrator'),
        ('OW', 'Owner')
    )

    uuid_id = models.UUIDField(
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
