from django.db import models
from django.utils import timezone
from patients.models import Patient #FK
from room.models import Room  #FK
from doctor.models import Doctor  #FK


class Admission(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete = models.CASCADE,
        db_column = 'IHI'
        
    )
    
    room = models.ForeignKey(
        Room,
        on_delete = models.CASCADE,
        db_column = 'room_id'
    )
    
    
    doctor = models.ForeignKey(
        Doctor,
        on_delete = models.CASCADE,
        db_column = 'doctor_id'
    )

    admitted_at = models.DateField(default=timezone.now)
    discharged_at = models.DateField(default=timezone.now)
    admission_reason = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    
    
    class Meta:
        db_table = 'admission'
        managed = False
        
        
    def __str__(self):
        return f"Patient {self.patient} admitted to Room {self.room}"
