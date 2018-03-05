from .models import Property
from .serializers import PropertySerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter


# Implementation of class-based-views for property objects
# - http://www.django-rest-framework.org/tutorial/3-class-based-views/
# Property-List
# GET - response returns all properties - any user can access
# POST - adds a single property to the database - authenticated or admin/tenant user only
class PropertyList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # Addition of filtering options (search query and ordering functionality)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('street_address', 'suburb', 'region', 'city')
    ordering_fields = ('__all__')


# Property-Detail
# PUT - updates a single property in the database - admin only (to be extended once landlords are added)
# GET - response returns a single property (by property id) - any user can access
# DELETE - deletes a single property - admin only (to be extended once landlords are added)
class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Property.objects.all()
    serializer_class = PropertySerializer
