from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    home_address = models.TextField()
    id_card_front = models.FileField(upload_to='id_cards/')
    id_card_back = models.FileField(upload_to='id_cards/')
    ssn_number = models.CharField(max_length=11)  # Be cautious with SSN storage
    maximum_salary_monthly = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
#  from django.db import models

class Plan(models.Model):
    DURATION_CHOICES = [
        ('3-5_days', '3-5 Days'),
        ('3-5_weeks', '3-5 Weeks'),
    ]
    
    duration = models.CharField(
        max_length=20,
        choices=DURATION_CHOICES,
        unique=True,
        help_text="Choose the duration of the plan."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter the price of the plan."
    )
    discount = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Add a discount description (if any)."
    )

    def __str__(self):
        return f"{self.get_duration_display()} - ${self.price}"
