from django.db import models

class Patient(models.Model):
    ihi = models.TextField(primary_key=True, db_column = "IHI")
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.TextField()
    phone_number = models.TextField()
    home_number = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    emergency_contact_name = models.TextField()
    emergency_contact_phone = models.TextField()
    date_registered = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateTimeField()
    
    class Meta:
        db_table = 'patient'
        managed = False
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"