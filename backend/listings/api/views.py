from .serializers import ListingSerializer, AreaSerializer, BoroughSerializer, BoroughBorderSerializer
from listings.models import Listing, Area, Borough, BoroughBorder
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer


class ListingCreate(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    parser_classes = (MultiPartParser, FormParser)


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    parser_classes = (MultiPartParser, FormParser)


class ListingDetail(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDelete(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingUpdate(generics.UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class BoroughList(generics.ListAPIView):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer

class BoroughCreate(generics.CreateAPIView):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer


class BoroughDetail(generics.RetrieveAPIView):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer
    lookup_field = "id"


class BoroughViewSet(viewsets.ModelViewSet):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer


class BoroughDeleteAllView(generics.GenericAPIView):
    serializer_class = BoroughSerializer

    def delete(self, request, *args, **kwargs):
        count, _ = Borough.objects.all().delete()
        return Response(
            {"message": f"Deleted {count} borough(s)"}, status=status.HTTP_200_OK
        )


class BoroughBorderViewSet(viewsets.ModelViewSet):
    queryset = BoroughBorder.objects.all()
    serializer_class = BoroughBorderSerializer
