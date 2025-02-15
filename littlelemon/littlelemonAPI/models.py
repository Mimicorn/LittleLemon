from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0)], db_index=True)
    inventory = models.PositiveSmallIntegerField(db_index=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return (f"{self.title} : {self.price}")
