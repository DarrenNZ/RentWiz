from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from tenantprofile.models import Tenant


# Serializer for the User Model
# - New Boston Tutorial: https://www.youtube.com/watch?v=V4NjlXiu5WI
class UserSerializer(serializers.ModelSerializer):
    # Ensure the password field is write-only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'tenantprofile:tenant-detail',
            },
            # Removal of the username uniqueness validator required to facilitate tenant/user updates
            # - Need to enforce username uniqueness when modifying username only
            # - Further work required to ensure username uniqueness is preserved
            # https://medium.com/django-rest-framework/dealing-with-unique-constraints-in-nested-serializers-dade33b831d9
            'username': {
                'validators': [UnicodeUsernameValidator()]
            }
        }


# Serializer for the Tenant-User Model (i.e. leveraging 1-to-1 relationship)
# - Related user class has been nested
# - Django Rest Framework Docs: http://www.django-rest-framework.org/api-guide/relations/
class TenantSerializer(serializers.ModelSerializer):
    # Link into the associated User object
    user = UserSerializer(required=True)

    class Meta:
        model = Tenant
        fields = ('user', 'id', 'phone', 'profile_picture', 'payment_method', 'payment_token')

    def create(self, validated_data):
        """
        Create and return a new 'Tenant-User' instance, given the validated data
        :param validated_data: data to be validated prior to creation of Tenant-User object
        :return: the Tenant-User serializer instance (often rendered as response to a view method)
        """
        # 1) Create User instance
        user_data = validated_data.pop('user', None)
        user = User.objects.create(password=make_password(user_data.pop('password')), **user_data)
        # 2) Create Related tenant instance
        return Tenant.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Tenant-User' instance, given the validated data
        :param instance: a serializer instance (i.e. data not stored in non-serialized format
        :param validated_data: data which has been validated and deserialized 
        :return: the final serializer instance (often rendered as response to a view method)
        """

        # Extract user nested-object
        user_data = validated_data.pop('user')

        # Update tenant specific details
        instance.phone = validated_data.get('phone', instance.phone)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.payment_token = validated_data.get('payment_token', instance.payment_token)

        # Update user nested-object
        instance.user.username = user_data.get('username')
        instance.user.email = user_data.get('email')
        instance.user.first_name = user_data.get('first_name')
        instance.user.last_name = user_data.get('last_name')
        # ... Check if password has changed, and if so...
        instance.user.password = make_password(user_data.get('password'))

        # Save tenant instance
        instance.user.save()
        instance.save()

        return instance
