from rest_framework import serializers
from .models import Property, PropertyStatus


class PropertyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyStatus
        fields = ('status',)


class PropertySerializer(serializers.ModelSerializer):
    status = PropertyStatusSerializer(required=True)

    class Meta:
        model = Property
        fields = (
            'id', 'street_address', 'suburb', 'region', 'city', 'postcode', 'bathrooms', 'tenant_capacity',
            'description', 'tag',
            'bedrooms',
            'price', 'date_added', 'date_sold', 'property_picture', 'status')

    def create(self, validated_data):
        """
        Create and return a new 'Property' instance, given the validated data
        :param validated_data: data to be validated prior to creation of Property object
        :return: the Property serializer instance (often rendered as response to a view method)
        """
        # 1) Create property instance
        serialized_status = validated_data.pop('status')
        status = PropertyStatus.objects.get(status=serialized_status['status'])
        return Property.objects.create(status=status, **validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Tenant-User' instance, given the validated data
        :param instance: a serializer instance (i.e. data not stored in non-serialized format
        :param validated_data: data which has been validated and deserialized 
        :return: the final serializer instance (often rendered as response to a view method)
        """

        # Extract status nested-object
        serialized_status = validated_data.pop('status')
        status = PropertyStatus.objects.get(status=serialized_status['status'])

        # Update property specific details
        instance.street_address = validated_data.get('street_address', instance.street_address)
        instance.suburb = validated_data.get('suburb', instance.suburb)
        instance.region = validated_data.get('region', instance.region)
        instance.city = validated_data.get('city', instance.city)
        instance.postcode = validated_data.get('postcode', instance.postcode)
        instance.bathrooms = validated_data.get('bathrooms', instance.bathrooms)
        instance.tenant_capacity = validated_data.get('tenant_capacity', instance.tenant_capacity)
        instance.description = validated_data.get('description', instance.description)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
        instance.price = validated_data.get('price', instance.price)
        instance.date_added = validated_data.get('date_added', instance.date_added)
        instance.date_sold = validated_data.get('date_sold', instance.date_sold)
        instance.property_picture = validated_data.get('property_picture', instance.property_picture)

        # Update status nested-object
        instance.status = status

        # Save property instance
        instance.status.save()
        instance.save()

        return instance
