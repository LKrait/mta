from django.db import models
import datetime
import random
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


class MorobeAdministrationDrivingPermit(models.Model):
    """
    Needs further information and improvement
    Information on type of application or formal
    documents necessary to obtain such permit.


    """
    # Database information
    db_id = models.CharField(max_length=20, default=generate_db_id)
    madp_id = models.CharField(max_length=20, default=generate_id)
    # Permit Holder
    name = models.CharField(max_length=255)
    division = models.CharField(max_length=255,
                                choices=[('PAO', "PA'S OFFICE"), ("MTR", 'MOTOTR TRAFFIC REGISTRY'),
                                         ('LFS', 'LAE FIRE STATION')])
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Exp', 'Expired'), ('Val', 'Valid'), ('Sup', 'Suspended')])
    # Date and data entry information
    date_updated = models.DateTimeField(auto_now=True)
    officer = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.madp_id} {self.name}'
