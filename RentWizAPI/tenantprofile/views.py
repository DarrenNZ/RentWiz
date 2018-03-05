from rest_framework import generics
from tenantprofile.models import Tenant
from tenantprofile.serializers import TenantSerializer
from rest_framework import permissions
from tenantprofile.permissions import IsPostOrIsAuthenticated


# Implementation of class-based-views for tenant profiles
# - http://www.django-rest-framework.org/tutorial/3-class-based-views/
# Tenant-List
# GET - response returns all tenants (admin only)
# POST - adds a single tenant to the database
class TenantList(generics.ListCreateAPIView):
    # Allow tenants to register but not view all tenants unless authenticated
    # - To be modified with custom permissions at later stage
    # - Most likely GET restricted to staff only or staff/landlords
    # - If tenantprofile app is extended to include wider user types
    #   it will be necessary to restrict query set by filtering
    #   example filter -> user_type="tenant" or equivalent
    permission_classes = (IsPostOrIsAuthenticated,)
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


# Tenant-Detail
# PUT - updates a single tenant in the database
# GET - response returns a single tenant
# DELETE - deletes a single tenant
class TenantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
