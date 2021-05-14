import time
import random
import datetime
from django.db import models


PROVINCE = [
    ('MBE', 'Morobe'), ('MDG', 'Madang'), ('EHP', 'Eastern Highlands'),('NCD', 'National Capital District')
]

def generate_id():
    """
    Genearting permit id, using randomly generated unique values
    :return:
    """
    date_stamp = datetime.datetime.now()
    month_id = date_stamp.strftime('%m%d')
    seq1 = random.randrange(100, 999, 1)
    year_id = date_stamp.strftime('%Y')
    seq2 = random.randrange(100, 999, 1)
    RESTEXT = str(month_id) + str(seq1) + str(year_id) + str(seq2)
    # datum.SERVER.append(RESTEXT)
    return RESTEXT


def generate_db_id():
    """

    :return:
    """
    time_stamp = str(time.time())
    rec_time = time_stamp.replace('.', '')
    rd = random.randrange(100, 999, 1)

    return rec_time+str(rd)


class Registration(models.Model):
    """

    Database model for deployment should include all necessary data to be used
    in a real-world application
    - Rego. No.
    - Vehicle Photo
    - etc,

    """
    db_id = models.CharField(max_length=50, default=generate_db_id)
    reg_id = models.CharField(max_length=50, default=generate_id)
    # Owners info
    full_name = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    residential_address = models.CharField(max_length=255)
    # Description of Vehicle
    vehicle_image = models.CharField(max_length=2058)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    body = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    engine_capacity = models.DecimalField(max_digits=6, decimal_places=0)
    engine_no = models.CharField(max_length=50)
    chassis_no = models.CharField(max_length=50)
    # USage of Vehicle
    uProv = models.CharField(max_length=50, choices=PROVINCE) # Province in which the vehicle is to be used
    UComm = models.CharField(max_length=50,
                             choices=[('1', 'Yes'), ('0', 'No')]) # If vehicle is to be used for commercial purpose
    # if Yes on commercial purposes
    # State Tare weight and Maximum Load
    tare_weight = models.DecimalField(max_digits=7, decimal_places=0, help_text='Weight to the nearest kilogram (kg)')
    maximum_load = models.DecimalField(max_digits=7, decimal_places=0, help_text='Weight to the nearest kilogram (kg)')
    # Officer updating the particular record, and date and time of record entry
    #  officerid to be sourced from account logon details
    officer = models.CharField(max_length=50)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reg_id
