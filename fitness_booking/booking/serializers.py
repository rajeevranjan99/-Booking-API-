from rest_framework import serializers
from .models import FitnessClass, Booking
import pytz

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Convert to IST for representation
        ist = pytz.timezone('Asia/Kolkata')
        rep['date_time'] = instance.date_time.astimezone(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
        return rep

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
