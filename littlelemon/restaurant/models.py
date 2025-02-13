from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    booking_date = models.DateField(null=False, blank=False, db_index=True)
    
    class Meta:
        ordering = ['booking_date']
    
    def __str__(self):
        return f'{self.name} book on {self.booking_date} for {self.no_of_guests}'
    
class Menu(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], db_index=True)
    inventory = models.PositiveIntegerField(default=0, db_index=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title


    