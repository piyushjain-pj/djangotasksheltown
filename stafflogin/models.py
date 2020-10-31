from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.first_name


class UserRegistered(models.Model):
    user_type_choice = [
        ('us', 'USER'),
        ('po', 'Property Owner'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone_number = models.CharField(max_length=13)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    is_sheltown_verified = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to='images/')
    user_Type = models.CharField(max_length=2, choices=user_type_choice)
    identity_proof = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "Registered_Users"

    def __str__(self):
        return self.first_name


class PropertyOwner(models.Model):
    pro_onwer_desig = [
        ('ow', 'Owner'),
        ('ma', 'Manager')
    ]
    whatsapp_number = models.CharField(max_length=50)
    Property_owner_designation = models.CharField(
        max_length=2, choices=pro_onwer_desig)
    cancelled_cheque = models.ImageField(upload_to="images/")
    bank_account_number = models.CharField(max_length=50)
    user_profile = models.ForeignKey("stafflogin.UserRegistered", verbose_name=(
        "phone_number"), on_delete=models.CASCADE)

    def __str__(self):
        return self.whatsapp_number

''''
class PropertiesListed(models.Model):
    property_status=[
        ('no','NOT AVAILABLE')
        ('yes','AVAILABLE')
        ]
    Property_Type_choices = [
        ('1','Flat/Apartment 1BHK'),
        ('2', 'Flat/Apartment 2BHK'), ('3', 'Flat/Apartment 3BHK'),
         ('4','Flat/Apartment 4BHK'), ('5', 'House'),
        ('6', 'PG/Hostel +1 Mate'), ('7', 'PG/Hostel + 2 Mate'),
        ('8', 'PG/Hostel +3 Mate'), ('9', 'PG/Hostel + 4 Mate')
    ]
    genderres_choices=[
        ('F', 'FAMILY +'),
        ('Fplus', 'Female'),
        ('Fonly','Female Only'),
        ('Monly', 'Male Only'),
    ]

    Name = models.CharField(max_length=100)
    Status = models.CharField(max_length=2,choices=property_status)
    PropertyType = models.CharField(max_length=2, choices=Property_Type_choices)
    TotalNoOfBeds = models.IntegerField()
    GenderRestrictions = models.CharField(
        max_length=50, choices=genderres_choices)
    Ownerstays = models.BooleanField(("Owners Stays"))

'''

