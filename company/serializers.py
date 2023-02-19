from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Сериализатор для компаний"""
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('debt', )
