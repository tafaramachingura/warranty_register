# warranty_api/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .authentication import tokenAuthentication
from rest_framework.views import APIView as APIVIEW
from django.contrib.auth.models import User
from .models import Asset
from .serializers import AssetSerializer


class AssetViewSet(viewsets.ModelViewSet):
    authentication_classes = [tokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([tokenAuthentication])
def register_warranty(request):
    try:
        data = request.data

        asset, created = Asset.objects.update_or_create(
            asset_id=data['asset_id'],
            defaults={
                "asset_name": data["asset_name"],
                "serial_number": data["serial_number"],
                "purchase_date": data["purchase_date"],
                "registered_by": request.user,
                 "registrant":data["real_name"],
                "status": "warranty_registered",
            }
        )

        return Response({
            "status": 'success',
            "message": "Warranty registered successfully" if created else "Warranty updated",
            "asset_id": asset.asset_id
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return Response({"error": str(e)}, status=400)
    



