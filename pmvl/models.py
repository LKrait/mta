from django.db import models
import random
import datetime
import time


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
    #datum.SERVER.append(RESTEXT)
    return RESTEXT


def generate_db_id():
    """

    :return:
    """
    time_stamp = str(time.time())
    rec_time = time_stamp.replace('.', '')
    rd = random.randrange(100, 999, 1)

    return rec_time+str(rd)



class PmvLicence(models.Model):
    """
    PMV Licence Validity to be includede in podction-based
    model database,
    valid = {}
    period = () in years
    status = (Expired, Valid, Suspended, etc)
    comments = (Remarks for consideration)
    """
    # Database Identification datum
    db_id = models.CharField(max_length=20, default=generate_db_id)
    pmv_licence_id = models.CharField(max_length=20, default=generate_id)
    # Owner's Information
    owner = models.CharField(max_length=255)
    occupation = models.CharField(max_length=20)
    place_of_birth = models.CharField(max_length=255)
    province = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    # addresses
    postal_address = models.CharField(max_length=255)
    residential = models.CharField(max_length=255)
    # Description
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    mileage = models.DecimalField(max_digits=10, decimal_places=0)
    # Passesnger information
    maximum_passenger = models.DecimalField(max_digits=4, decimal_places=0)
    # Routes
    authorized_route = models.CharField(max_length=20,
                                        choices=[('R1', 'Route 1'), ('R2', 'Route 2'), ('R3', 'Route 3'), ('R100', 'Route 100')])
    other_routes = models.CharField(max_length=20,
                                    choices=[('17A', 'Market-Town-Malahang'), ('11C', 'Market-Town-Taraka'), ('14B', 'Town-Eriku-4 Mile')])
    # Date entry, Officer entry
    date_updated = models.DateTimeField(auto_now=True)
    officer = models.CharField(max_length=20)

    def __str__(self):
        return self.db_id
