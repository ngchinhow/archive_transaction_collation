from django.db import models


class DocparserMapper(models.Model):
    objects = models.Manager()

    display_name = models.CharField(max_length=100)
    docparser_label_name = models.CharField(max_length=100)


class Transaction(models.Model):
    objects = models.Manager()

    post_date = models.DateField()
    transaction_date = models.DateField()
    description = models.CharField(max_length=400)
    reference = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
