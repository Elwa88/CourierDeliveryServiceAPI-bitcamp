from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
    ProofViewSet,
    CustomUserViewSet,
    ParcelViewSet,
    AssignedParcels,
)
router = DefaultRouter()
router.register(r'parcels',ParcelViewSet)
router.register(r'users',CustomUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/parcels/<int:id>/delivery_proof/',ProofViewSet.as_view({'post': 'create','get' : "list"}), name = 'proofs'),
    path('api/courier/',AssignedParcels.as_view(), name= 'courier'),
]
