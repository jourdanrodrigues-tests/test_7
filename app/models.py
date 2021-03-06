from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _
from rest_framework.authtoken.models import Token


class AbstractUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractUUIDModel):
    def get_token(self):
        if hasattr(self, 'auth_token'):
            return self.auth_token
        else:
            return Token.objects.create(user=self)


class Pizza(AbstractUUIDModel):
    # Picture lots of attributes
    pass


class Order(AbstractUUIDModel):
    THIRTY_CM_PIZZA = 1
    FIFTY_CM_PIZZA = 2
    PIZZA_SIZE_CHOICES = (
        (THIRTY_CM_PIZZA, _('30cm pizza')),
        (FIFTY_CM_PIZZA, _('50cm pizza')),
    )

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    pizza_size = models.PositiveSmallIntegerField(choices=PIZZA_SIZE_CHOICES)
