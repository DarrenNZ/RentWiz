from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAdminUser

# View definition for API root
# - Generic form for new app>models
# - '<endpoint>': reverse('<endpoint>:<endpoint-name>', request=request, format=format)
@api_view(['GET'])
@permission_classes((IsAdminUser, ))
def api_root(request, format=None):
    return Response({
        'tenantprofile': reverse('tenantprofile:tenant-list', request=request, format=format),
        'property': reverse('property:property-list', request=request, format=format)
    })