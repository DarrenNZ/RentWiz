from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tenantprofile import views

app_name = "tenant_profile"

urlpatterns = [
    # URL roots for the tenantprofile app
    # - generic format url(r'<route-name>^$', <view>',name='<endpoint-name>'))
    url(r'^tenants/$', views.TenantList.as_view(), name='tenant-list'),
    url(r'^tenants/(?P<pk>[0-9]+)/$', views.TenantDetail.as_view(), name='tenant-detail'),
]
