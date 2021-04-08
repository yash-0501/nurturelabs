from rest_framework import serializers
from .models import Advisor, Booking
from authentication.models import User

class addAdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advisor
        fields = ['name','profile_pic','id']

    def validate(self, attrs):

        name = attrs.get('name','')
        profile_pic = attrs.get('profile_pic','')

        return attrs

    def create(self, validated_data):
        return Advisor.objects.create(**validated_data) #creates an advisor - only by admin


class advisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advisor
        fields = ['name','profile_pic','id']


class bookAdvisorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['booking_time','user','advisor']
    
    def validate(self, attrs):

        booking_time = attrs.get('booking_time','')

        return attrs

    def create(self, validated_data):
        return Booking.objects.create(**validated_data) #creates a new booking

class listAllBookingsSerializer(serializers.ModelSerializer):
    advisor = advisorSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ['user','booking_time','advisor']

    

    