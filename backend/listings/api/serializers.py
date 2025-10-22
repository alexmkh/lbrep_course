from rest_framework import serializers
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from listings.models import Listing, Poi, Area, Borough, BoroughBorder


class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    listing_pois_within_10km = serializers.SerializerMethodField()

    def get_listing_pois_within_10km(self, obj):
        listing_location = Point(obj.latitude, obj.longitude, srid=4326)
        query = Poi.objects.filter(location__distance_lte=(listing_location, D(km=10)))
        query_serialized = PoiSerializer(query, many=True)
        return query_serialized.data

    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name

    def get_seller_username(self, obj):
        return obj.seller.username

    def get_country(self, obj):
        return "England"

    class Meta:
        model = Listing
        fields = "__all__"


class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = "__all__"

    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    def get_latitude(self, obj):
        return obj.location.tuple[0] if obj.location else None

    def get_longitude(self, obj):
        return obj.location.tuple[1] if obj.location else None


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"

    # boroughs = serializers.StringRelatedField(many=True)
    boroughs = serializers.SerializerMethodField()
    def get_boroughs(self, obj):
        query = Borough.objects.filter(area=obj)
        boroughs_serialized = BoroughSerializer(query, many=True)
        return boroughs_serialized.data


class BoroughBorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoroughBorder
        geo_field = "border"
        fields = ["id", "border", "borough"]


class BoroughSerializer(serializers.ModelSerializer):
    area = serializers.SlugRelatedField(slug_field="name", queryset=Area.objects.all())
    border = BoroughBorderSerializer(source="border_data", read_only=True)

    class Meta:
        model = Borough
        fields = "__all__"
        # read_only_fields = ["id"]
