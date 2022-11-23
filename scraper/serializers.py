
from rest_framework import serializers

from scraper.models import PartsDetails


class PartsDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartsDetails
        fields = ['id', 'company_name', 'category_name', 'model_name',
                  'part_name']
