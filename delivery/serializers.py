from rest_framework import serializers
from .models import (
    CustomUser,
    Parcel,
    DeliveryProof
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser(username = validated_data['username'],
                          role = validated_data['role'],)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'
        read_only_fields = ['sender']

class DeliveryProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProof
        fields = '__all__'
