from rest_framework import serializers
from . models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    This class specifies which fields need to be serialized.
    It can also be set to only include certain fields like:
    > fields = ('first_name', 'last_name' 'job_title')
    """
    class Meta:
        model = Employee
        fields = '__all__'
