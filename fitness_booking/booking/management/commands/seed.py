from django.core.management.base import BaseCommand
from booking.models import FitnessClass
from datetime import datetime, timedelta
import pytz

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ist = pytz.timezone('Asia/Kolkata')
        FitnessClass.objects.all().delete()
        classes = [
            {"name": "Yoga", "instructor": "Aarti", "days_from_now": 1},
            {"name": "Zumba", "instructor": "Raj", "days_from_now": 2},
            {"name": "HIIT", "instructor": "Meera", "days_from_now": 3},
        ]

        for c in classes:
            dt = datetime.now(ist) + timedelta(days=c["days_from_now"])
            utc_dt = dt.astimezone(pytz.UTC)
            FitnessClass.objects.create(
                name=c["name"],
                instructor=c["instructor"],
                date_time=utc_dt,
                total_slots=10,
                available_slots=10
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded classes!'))
