from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from property import views

app_name = "property"

urlpatterns = [
    # URL roots for the landlordprofile app
    # - generic format url(r'^', include('<app-name>.urls', namespace='<endpoint-name>'))
    url(r'^properties/$', views.PropertyList.as_view(), name='property-list'),
    url(r'^properties/(?P<pk>[0-9]+)/$', views.PropertyDetail.as_view(), name='property-detail'),
]
