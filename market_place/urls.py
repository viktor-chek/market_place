from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('company.urls')),

    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger',
         SpectacularSwaggerView.as_view(url_name='schema'))
]
