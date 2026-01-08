from django.db import models

# Create your models here.
class Ward(models.Model):
    name = models.TextField()
    floor = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = 'ward' #Table name in the database (PostgreSQL)
        managed = False
        
    def __str__(self):
        return self.name 