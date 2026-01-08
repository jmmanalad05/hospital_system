from django.db import models
from django.utils import timezone
from specialization.models import Specialization

# Create your models here.
class Doctor(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    date_hired = models.DateField(default=timezone.now)
    
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        db_column ='specialization_id'
    )
    
    class Meta:
        db_table = 'doctor'
        managed = False
        
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
    
    