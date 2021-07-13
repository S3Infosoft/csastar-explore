from django.db import models

# Create your models here.
class Companies(models.Model):
    CompanyName = models.CharField(max_length=300)
    ListedSince = models.DateField()
    LastUpdated = models.DateField()
    Level = models.CharField(max_length=300)
    Description = models.TextField()
    Attachment = models.CharField(max_length=300)
    Filename = models.FileField(upload_to=None, max_length=300,blank=True,null=True)

    def __str__(self):
        return self.CompanyName

class caiq_company_map(models.Model):
    CompanyID = models.ForeignKey(Companies, on_delete=models.CASCADE)
    CAIQResponseVersions= models.CharField(max_length=300)