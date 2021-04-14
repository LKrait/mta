from django.db import models
import random
import datetime
from . import datum
import time
from . datum import SERVER


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
    datum.SERVER.append(RESTEXT)
    return RESTEXT


def generate_db_id():
    """

    :return:
    """
    time_stamp = str(time.time())
    rec_time = time_stamp.replace('.', '')
    rd = random.randrange(100, 999, 1)

    return rec_time+str(rd)


class LearnersPermit(models.Model):
    """

    """
    # db_id to be used to append list in a seperate data file
    # db_id to be used as entry reference
    #
    db_id = models.CharField(max_length=20, default=generate_db_id)
    permit_id = models.CharField(max_length=15, default=generate_id)
    licence_class = models.CharField(max_length=10)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50,)
    postal_address = models.CharField(max_length=255)
    # Permit applicant description
    # needs to be seperated from learners permit model for the production model system
    # Description
    age = models.DecimalField(max_digits=3, decimal_places=0)
    height = models.DecimalField(max_digits=3, decimal_places=0)
    eyes = models.CharField(max_length=10)
    complexion = models.CharField(max_length=10)
    # models photo to be included as well
    updated = models.DateTimeField(auto_now=True)
    #
    # Officer ID is automatically generated using account login details, privilleges , etc.
    officer_id = models.CharField(max_length=20,
                                  choices=[('Officer - Admin', 'OAD'), ('Officer-Licencing', 'OLC'),
                                           ('Officer - Technical', 'OTC'), ('Superintendent', 'SPT'),
                                           ('Officer - TIN', 'OTN')
                                           ])

    def __str__(self):
        """

        :return:
        """
        SERVER.append(self.db_id)
        return f'{self.permit_id} - {str(self.surname).upper()} {self.given_name}'

