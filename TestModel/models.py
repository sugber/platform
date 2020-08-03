# models.py
from django.db import models


class aizuji ( models.Model ) :
    db_table = 'aizuji_user'
    casename = models.CharField ( max_length=20 )
    data = models.CharField ( max_length=20 )
    url = models.CharField ( max_length=20 )
    method = models.CharField ( max_length=20 )
    type = models.CharField ( max_length=20 )