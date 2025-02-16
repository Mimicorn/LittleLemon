from rest_framework.test import APIClient, APITestCase
from restaurant.models import Menu
from django.urls import reverse

class MenuItemTest(APITestCase):
    def setUp(self):
        Menu.objects.create(title='Beef noodles', price=8.5, inventory=20)
        Menu.objects.create(title='Spring rolls', price=6.5, inventory=100)
        Menu.objects.create(title='Fried shrimp', price=8, inventory=30)
    
        self.client = APIClient()
    
    def test_create_menu_view(self):
        url = reverse('menu_view')
        menuitem = {'title': 'Pizza', 'price': 10, 'inventory': 50}
        response = self.client.post(url, data=menuitem, format='json')
        
        response_data = response.data.copy()
        response_data.pop('id', None)
        
        self.assertEqual(response.status_code, 201)
        
        expected = {'title': 'Pizza', 'price': '10.00', 'inventory': 50}
        
        self.assertEqual(response_data, expected)
        
        self.assertTrue(Menu.objects.filter(title='pizza').exists())

    def test_list_menu_view(self):
        url = reverse('menu_view')
        response = self.client.get(url)
        response_data = response.data.copy()
        for item in response_data:
            item.pop('id', None)
        
        self.assertEqual(response.status_code, 200)
        
        expected = [
            {'title': 'Beef noodles', 'price': '8.50', 'inventory': 20},
            {'title': 'Spring rolls', 'price': '6.50', 'inventory': 100},
            {'title': 'Fried shrimp', 'price': '8.00', 'inventory': 30}
        ]
        self.assertEqual(response_data, expected)
        
        
        
        
