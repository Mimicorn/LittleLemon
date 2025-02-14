from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
#    def get(self, request, *args, **kwargs):
#        pass
    
#    def post(self, request, *args, **kwargs):
#        pass
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]