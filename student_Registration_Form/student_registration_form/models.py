from django.db import models


# Database created for PDF file
class pdf_file(models.Model):
    name = models.CharField(max_length=100)
    pdffile = models.FileField()

    def __str__(self):
        return self.name

# Database created for Teacher info
class TeachersInfo(models.Model):
    Username = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100) 
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Username