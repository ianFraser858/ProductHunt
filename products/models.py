from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    title = models.TextField(max_length=200)
    product_url = models.URLField(default='none')
    pub_date = models.DateTimeField(default=timezone.now)
    vote_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=200)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')