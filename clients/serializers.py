from rest_framework import serializers
from clients.models import Client, ClientImage


# Image model serializer
class ClientImageSerializer(serializers.ModelSerializer):

    # Image crop settings
    left = serializers.IntegerField(min_value=0)
    top = serializers.IntegerField(min_value=0)
    right = serializers.IntegerField(min_value=0)
    bottom = serializers.IntegerField(min_value=0)

    class Meta:
        model = ClientImage
        fields = ('image', 'left', 'top', 'right', 'bottom')

    # Custom validation
    def validate(self, attrs):
        # Check if crop settings are valid
        if attrs['left'] >= attrs['right'] or attrs['top'] >= attrs['bottom']:
            raise serializers.ValidationError("Invalid crop settings")
        return attrs

    # Custom representation
    def to_representation(self, instance):
        representation = {'image': self.get_image_url(ClientImage.objects.get(pk=instance.pk))}
        return representation

    # Get image url path
    def get_image_url(self, image):
        request = self.context.get('request')
        photo_url = image.image.url
        return request.build_absolute_uri(photo_url)


# Client model serializer
class ClientSerializer(serializers.ModelSerializer):

    # Add custom field
    clientimage = ClientImageSerializer()

    class Meta:
        model = Client
        fields = '__all__'

    # Add ClientImage to create method
    def create(self, validated_data):
        client_img = validated_data.pop('clientimage')
        crops = (client_img['left'], client_img['top'], client_img['right'], client_img['bottom'])
        instance = Client.objects.create(**validated_data)
        image = ClientImage.objects.create(image=client_img['image'], client=instance)
        image.save(crop_values=crops)
        return instance

    # Add ClientImage to update method
    def update(self, instance, validated_data):
        client_img = validated_data.pop('clientimage')
        crops = (client_img['left'], client_img['top'], client_img['right'], client_img['bottom'])
        Client.objects.filter(pk=instance.pk).update(**validated_data)
        image = ClientImage.objects.update_or_create(client=instance, defaults={'image': client_img['image']})
        image[0].save(crop_values=crops)
        return Client.objects.get(pk=instance.pk)
