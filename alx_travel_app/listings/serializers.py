from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'location',
            'price_per_night',
            'owner',
            'created_at',
        ]

class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'user',
            'check_in',
            'check_out',
            'guests',
            'created_at',
        ]

class ReviewSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'listing',
            'user',
            'rating',
            'comment',
            'created_at',
        ]