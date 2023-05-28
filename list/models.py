from django.db import models

class VoterList(models.Model):
    district = models.CharField(max_length=100)
    assembly_constituency = models.CharField(max_length=100)
    part = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='voter_lists/')

    def __str__(self):
        return f"{self.district} - {self.assembly_constituency} - {self.part}"
