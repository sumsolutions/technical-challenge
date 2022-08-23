from trading.serializers import BlotterSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from trading.models import Blotter


class BlotterViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving blotters data.
    """

    def list(self, request):
        queryset = Blotter.objects.all()
        serializer = BlotterSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)
