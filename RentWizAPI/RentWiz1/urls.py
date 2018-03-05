from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as root_views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    # Route for admin console
    path('admin/', admin.site.urls),

    # API root route
    url(r'^$', root_views.api_root),


    # API authentication endpoint
    # - http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    url(r'^api-token-auth/', auth_views.obtain_auth_token, name='auth'),

    # API route.py inclusions
    # - generic format url(r'^', include('<app-name>.urls', namespace='<endpoint-name>'))
    url(r'^', include('tenantprofile.urls', namespace="tenantprofile")),
    url(r'^', include('property.urls', namespace="property")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
