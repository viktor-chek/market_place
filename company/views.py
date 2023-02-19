from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from company.models import Company
from company.permissions import EmployeesPermission
from company.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """Вьюсет компаний"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [EmployeesPermission]
