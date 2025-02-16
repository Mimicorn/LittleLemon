from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(title='Kebab', price=10, inventory=25)
        self.assertEqual(item.__str__(), "Kebab : 10")
    
    def test_update_item(self):
        item = Menu.objects.create(title='Greek salad', price=7.5, inventory=30)
        count = Menu.objects.filter(title__icontains='Greek salad').update(price=6)
        item = Menu.objects.get(title='Greek salad')
        self.assertEqual(item.price, 6)
        
class BookingTest(TestCase):
    def test_add_booking(self):
        booking = Booking.objects.create(name='testname', no_of_guests=6, booking_date='2025-03-01')
        self.assertEqual(booking.__str__(), "testname book on 2025-03-01 for 6")