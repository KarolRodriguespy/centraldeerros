import collections
from itertools import groupby
from operator import itemgetter

from django.db.models import Q

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import validate_ipv4_address

LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

ENVIRONMENT_CHOICES = [
    ('produção', 'produção'),
    ('homologação', 'homologação'),
    ('dev', 'dev'),

]


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES)
    log = models.TextField(max_length=500)
    address = models.GenericIPAddressField(validators=[validate_ipv4_address])
    date = models.DateField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    objects = models.Manager()

    @property
    def count_events(self):
        if self.level == self.level:
            return Event.objects.values('log').count()


    def __str__(self):
        return f'{self.level} - {self.count_events}'
