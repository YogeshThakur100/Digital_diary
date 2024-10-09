from django.db import models

# Create your models here.

class niradhar(models.Model):
    client_name = models.CharField(max_length= 100 , null=False)
    client_number = models.IntegerField(default=0)
    Amount = models.IntegerField(default=5000)
    aadhar = models.BooleanField(default=False)
    pancard = models.BooleanField(default=False)
    income_certificate = models.BooleanField(default=False)
    voterid = models.BooleanField(default=False)
    passport = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name
