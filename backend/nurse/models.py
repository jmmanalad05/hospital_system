from django.db import models
from django.utils import timezone
from ward.models import Ward

class Nurse(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    date_hired = models.DateField(default=timezone.now)
    
    ward = models.ForeignKey(
        Ward,
        on_delete = models.CASCADE,
        db_column = 'ward_id'
        
    )
    
    class Meta:
        db_table = 'nurse'
        managed = False
        
    def __str__(self):
        return f"RN.{self.first_name} {self.last_name}"