from rest_framework import serializers

from listings.models import Listing, Poi

class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    listing_pois = serializers.SerializerMethodField()

    def get_listing_pois(self, obj):
        query = Poi.objects.all()
        query_serialized = PoiSerializer(query, many=True)
        return query_serialized.data

    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name if hasattr(obj.seller, 'profile') else None

    def get_seller_username(self, obj):
        return obj.seller.username

    def get_country(self, obj):
        return "England"

    class Meta:
        model = Listing
        fields = '__all__'


class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = '__all__'

    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    def get_latitude(self, obj):
        return obj.location.tuple[0] if obj.location else None

    def get_longitude(self, obj):
        return obj.location.tuple[1] if obj.location else None

