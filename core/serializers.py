from django.db.models import fields
from rest_framework import serializers
from core.models import *


class CSVFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVFiles
        fields = ("csv_file", )


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = ("customer", "item", "total")
