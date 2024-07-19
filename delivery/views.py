from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .permissions import ParcelPermissions, ProofPermissions
from .models import Parcel, DeliveryProof, CustomUser
from .serializers import ParcelSerializer, DeliveryProofSerializer, CustomUserSerializer


class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [ParcelPermissions]

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