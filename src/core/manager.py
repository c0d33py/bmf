from django.db import models


class ServiceQuerySet(models.Manager):
    def get_queryset(self):
        return super(ServiceQuerySet, self).get_queryset().filter(status=True)
