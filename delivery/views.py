from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .permissions import (
    AdminPermissions,
    CustomerPermissions,
    CourierPermissions,
    ProofPermissions,
    )
from .models import Parcel, DeliveryProof, CustomUser
from .serializers import ParcelSerializer, DeliveryProofSerializer, CustomUserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','status','sender','courier','receiver_name']
    def get_permissions(self):
        user = self.request.user
        if not user.is_authenticated:
             permission_classes = [IsAuthenticated]
        elif user.role == "courier":
                permission_classes = [CourierPermissions]
        elif user.role == "customer":
                permission_classes = [CustomerPermissions]
        elif user.role == "admin":
             permission_classes = [AdminPermissions]

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
    def get_permissions(self):
        if self.action == 'create':
              permission_classes = [AllowAny]
        else:
              permission_classes = [IsAuthenticated,AdminPermissions]
        return [permission() for permission in permission_classes]

class AssignedParcels(APIView):
    def get(self,request):
        parcels = Parcel.objects.all()
        assigned_parcels = []
        for parcel in parcels:
            if parcel.courier == request.user:
                assigned_parcels.append(parcel)
        serializer = ParcelSerializer(assigned_parcels, many = True)
        return Response(serializer.data)