import random
from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Booking.objects.all().delete()
        Review.objects.all().delete()
        Listing.objects.all().delete()

        self.stdout.write('Creating listings...')
        listings = []
        for i in range(10):
            listing = Listing.objects.create(
                title=f'Cozy Apartment #{i + 1}',
                description='A nice and cozy place to stay.',
                price_per_night=random.uniform(50, 200),
                location='City Center'
            )
            listings.append(listing)

        self.stdout.write('Creating bookings and reviews...')
        for listing in listings:
            # Create bookings
            for j in range(random.randint(1, 5)):
                Booking.objects.create(
                    listing=listing,
                    user_name=f'User{j + 1}',
                    check_in=timezone.now().date() + timedelta(days=j * 7),
                    check_out=timezone.now().date() + timedelta(days=j * 7 + 3)
                )
            # Create reviews
            for k in range(random.randint(1, 3)):
                Review.objects.create(
                    listing=listing,
                    user_name=f'Reviewer{k + 1}',
                    rating=random.randint(1, 5),
                    comment='This is a great place!',
                    created_at=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
