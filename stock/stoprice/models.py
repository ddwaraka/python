from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class StockName(models.Model):
    company_code = models.CharField(max_length=250)
    target_price = models.FloatField(max_length=10)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (('company_code', 'user'),)

    def __unicode__(self):
        return "{0}, {1}".format(self.company_code, self.target_price)
