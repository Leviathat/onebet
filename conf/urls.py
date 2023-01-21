from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('api-schema/', get_schema_view(title='OneBET Schema'), name='api-schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        ),
        name='docs'),
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls', namespace='authentication')),
]
