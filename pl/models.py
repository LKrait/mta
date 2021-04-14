from django.db import models
import random
import datetime
import time


def generate_lid():
    """

    :return:
    """
    PROVINCE_CODE = 13
    date = datetime.datetime.now()
    date_stamp = date.strftime('%m%d')
    year = date.strftime('%Y')
    random_value = random.randrange(1000, 9999, 1)
    return str(PROVINCE_CODE)+str(date_stamp)+str(random_value)+str(year)[1:]


def generate_db_id():
    """

    :return:
    """
    time_stamp = str(time.time())
    rec_time = time_stamp.replace('.', '')
    rd = random.randrange(100, 999, 1)

    return rec_time+str(rd)


class Licence(models.Model):
    """

    """
    licence_id = models.CharField(max_length=15, default=generate_lid)
    db_id = models.CharField(max_length=20, default=generate_db_id)
    surname = models.CharField(max_length=50)
    given_names = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices =[
        ('Female', 'F'),
        ('Male', 'M')
    ])
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100) # Try using one to many fields types, search Town, automatically list districts etc..
    nationality = models.CharField(max_length=20, choices= [
        ('Citizen', 'Papua New Guinean'),
        ('Non-citizen', 'Expatriate')
    ])    # Find country list in a csv file
    # LICENCE TYPE
    licence_type = models.CharField(max_length=20, choices=[
        ('PNG-DL', "PNG Driver's Licence"), ('PNG-PDL', 'Provisional Licence')
    ])
    class_of_licence = models.CharField(max_length=20, choices=[
        ('1', 'One (1)'), ('2', 'Two (2)'), ('3', 'Three (3)'),
        ('4', "Four (4)"), ('5', 'Five (5)'), ('6', 'Six (6)'),
        ('7', 'Seven (7)')
    ])
    validity = models.DecimalField(max_digits=3, decimal_places=0)    # in years or monthd
    date_issued = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('SUS', 'Suspended'), ('CND', 'Cancelled'), ('VLD', 'Valid'),('EXP', 'Expired')
    ])         # Options for , cancelled, suspended, Valid, expired, etc...
    old_licence_number = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)   # To be modified to include date + logged-on user

    def __str__(self):
        return f'{self.licence_id} - {str(self.surname).upper()}  {self.given_names}'

