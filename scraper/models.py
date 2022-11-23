from django.db import models

# Create your models here.


class PartsDetails(models.Model):
    company_name = models.CharField(max_length=256)
    category_name = models.CharField(max_length=256)
    model_name = models.CharField(max_length=256)
    part_name = models.CharField(max_length=256)

    class Meta:
        db_table = "parts_details"
