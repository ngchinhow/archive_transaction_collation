from django.db import models


class Document(models.Model):
    objects = models.Manager()

    batch_id = models.UUIDField(primary_key=True, db_column='BatchID')
    id = models.CharField(max_length=32, db_column='ID')
    name = models.CharField(max_length=150, db_column='Name')
    processed = models.BooleanField(default=False, db_column='Processed')
    created_at = models.DateTimeField(auto_now_add=True, db_column='CreatedAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='UpdatedAt')
