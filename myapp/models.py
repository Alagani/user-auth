from django.db import models

# Create your models here.

class SignUp(models.Model):
    qq=models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)  # Store hashed passwords

    # You can add more fields as needed for the signup process
    # Additional fields might include: first_name, last_name, date_of_birth, etc.

    def __str__(self):
        return self.email  # Customize the string representation of the model
