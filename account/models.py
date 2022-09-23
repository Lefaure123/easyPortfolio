from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        pass




# non = models.CharField(max_length=50, blank=True, null=True)
    # siyati = models.CharField(max_length=50, blank=True, null=True)
    # imel = models.EmailField(max_length=100, blank=True, null=True)
    # foto = models.ImageField(upload_to='./Pictures', blank=True, null=True)
    # telefon = models.CharField(max_length=60, blank=True, null=True)
    # modpass = models.CharField(max_length= 70, blank=True, null=True)
