from django.db import models
from django.utils import timezone
from patients.models import Patient
from doctor.models import Doctor

class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete = models.CASCADE,
        db_column = 'doctor_id'
    )
    
    patient = models.ForeignKey(
        Patient,
        on_delete = models.CASCADE,
        db_column = 'IHI'
        
    )
    
    appointment_datetime = models.DateTimeField(auto_now=True)
    status = models.TextField()
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    
    class Meta:
        db_table = 'appointment'
        managed = False
        
    
    def __str__(self):
        return f"Patient: {self.patient} Appointment at: {self.appointment_datetime} with Dr. {self.doctor}"