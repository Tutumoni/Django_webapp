from django.db import models

# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_email = models.EmailField(unique=True)
    college_address = models.CharField(max_length=250)
    college_city = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name

    class Meta:
        db_table = 'college'