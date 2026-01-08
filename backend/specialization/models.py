from django.db import models

class Specialization(models.Model):
    name = models.TextField()
    
    class Meta:
        db_table = 'specialization'
        managed = False
        
    def __str__(self):
        return self.name
