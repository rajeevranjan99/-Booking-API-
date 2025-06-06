from django.test import TestCase
from .models import FitnessClass, Booking
from django.utils import timezone

class BookingTest(TestCase):
    def setUp(self):
        self.cls = FitnessClass.objects.create(
            name="Yoga",
            date_time=timezone.now(),
            instructor="Aarti",
            total_slots=5,
            available_slots=5
        )

    def test_booking_creation(self):
        response = self.client.post("/book", {
            "class_id": self.cls.id,
            "client_name": "Test User",
            "client_email": "test@example.com"
        }, content_type='application/json')
        self.assertEqual(response.status_code, 201)


# Create your tests here.
