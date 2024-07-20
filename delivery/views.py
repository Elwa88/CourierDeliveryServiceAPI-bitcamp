from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .permissions import (
    AdminPermissions,
    CustomerPermissions,
    CourierPermissions,
    ProofPermissions,
    )
from .models import Parcel, DeliveryProof, CustomUser
from .serializers import ParcelSerializer, DeliveryProofSerializer, CustomUserSerializer


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    def get_permissions(self):
        if self.action in ['list','partial_update', 'retrieve']:
            permission_classes = [CourierPermissions]
        if self.action in ['create', 'update','destroy']:
            permission_classes = [CustomerPermissions]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(sender = self.request.user)

class ProofViewSet(viewsets.ModelViewSet):
    queryset = DeliveryProof.objects.all()
    serializer_class = DeliveryProofSerializer
    permission_classes = [ProofPermissions]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class AssignedParcels(APIView):
    def get(self,request):
        parcels = Parcel.objects.all()
        assigned_parcels = []
        for parcel in parcels:
            if parcel.courier == request.user:
                assigned_parcels.append(parcel)
        serializer = ParcelSerializer(assigned_parcels, many = True)
        return Response(serializer.data)