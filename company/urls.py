from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from company.views import CompanyViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]
