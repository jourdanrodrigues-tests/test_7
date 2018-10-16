from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


class AbstractUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractUUIDModel):
    pass


class Order(AbstractUUIDModel):
    THIRTY_CM_PIZZA = 1
    FIFTY_CM_PIZZA = 2
    PIZZA_SIZE_CHOICES = (
        (THIRTY_CM_PIZZA, _('30cm pizza')),
        (FIFTY_CM_PIZZA, _('50cm pizza')),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    pizza_size = models.PositiveSmallIntegerField(choices=PIZZA_SIZE_CHOICES)
