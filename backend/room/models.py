from django.db import models
from ward.models import Ward
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    room_number = models.TextField()
    
    ward = models.ForeignKey(
        Ward,
        on_delete = models.CASCADE,
        db_column = 'ward_id'
    )
    room_type = models.TextField()
    floor = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    
    
    class Meta:
        db_table = 'room'
        managed = False
        
    def __str__(self):
        return f'Room Number: {self.room_number} on Floor: {self.floor}'