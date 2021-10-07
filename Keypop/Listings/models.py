from django.db import models
import uuid 
# Create your models here.
class Keyboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=30, null=True, blank=True, editable=True)
    material = models.CharField(max_length=30, null=True, blank=True, editable=True)
    color = models.CharField(max_length=30, null=True, blank=True, editable=True)
    layout = models.CharField(max_length=30, null=True, blank=True, editable=True)
    condition = models.CharField(max_length=30, null=True, blank=True, editable=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, editable=True)
    description = models.CharField(max_length=5000, null=True, blank=True, editable=True)
    negotiable = models.BooleanField(default=False, null=True, blank=True)
    trade = models.BooleanField(default=False, null=True, blank=True)
    RGB = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sold = models.BooleanField(default=False, null=True, blank=True)

    
    def __str__(self):
        return f'{self.model_name}'

class Switch(models.Model):
    switch_name = models.CharField(max_length=30, null=True, blank=True, editable=True)
    switch_type = models.CharField(max_length=30, null=True, blank=True, editable=True)
    spring_force = models.CharField(max_length=30, null=True, blank=True, editable=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, editable=True)
    amount = models.IntegerField( default=10, null=True, blank=True, editable=True)
    
    def __str__(self):
        return f'{self.switch_name}'

    class Meta:
        verbose_name_plural = "Switches"

class Keycap(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, editable=True)
    material = models.CharField(max_length=30, null=True, blank=True, editable=True)
    profile = models.CharField(max_length=30, null=True, blank=True, editable=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, editable=True)
    
    def __str__(self):
        return f'{self.profile} {self.name}'

    class Meta:
        verbose_name_plural = "Keycaps"