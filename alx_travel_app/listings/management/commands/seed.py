from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from random import randint, choice

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create a default user if not exists
        user, created = User.objects.get_or_create(username='demo_owner')
        if created:
            user.set_password('password123')
            user.save()

        sample_locations = ['Lagos', 'Abuja', 'Nairobi', 'Cape Town', 'Accra']
        sample_titles = [
            'Cozy Apartment in City Center',
            'Luxury Villa with Pool',
            'Budget Room Near Airport',
            'Beachfront Bungalow',
            'Modern Studio Flat'
        ]

        for i in range(10):
            Listing.objects.create(
                title=choice(sample_titles),
                description='Sample description for listing {}'.format(i+1),
                location=choice(sample_locations),
                price_per_night=randint(50, 500),
                owner=user
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded sample listings!'))