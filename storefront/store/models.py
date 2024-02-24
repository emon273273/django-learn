from django.db import models

# Create your models here.
class Product(models.Model):
    # sku=models.CharField(max_length=10,primary_key=True) #django auto create kore id kintu amra jodi chai je amra nijeder moto kore kaj korbo se khetere amra chaile alada kore evabeo kaj kore korte pari
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=4,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B',
    MEMBERSHIP_SILVER='S',
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
         (MEMBERSHIP_SILVER,'Silver'),
          (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)

    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=20)
    birth_date=models.DateField(null=True)
    membership_choices=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_STATUS_PENDING='P',
    PAYMENT_STATUS_COMPLETE='C',
    PAYMENT_STATUS_FAILED='F',
    PAYMENT_STATUS_CHOICES=[(PAYMENT_STATUS_FAILED,'Failed'),
                            (PAYMENT_STATUS_COMPLETE,'Completed'),
                            (PAYMENT_STATUS_PENDING,"Pending")]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
