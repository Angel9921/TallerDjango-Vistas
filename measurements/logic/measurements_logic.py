from ..models import Measurement
from ..models import Variable
from datetime import datetime

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()
    

def update_measurement(var_pk, var):
    measurement = Measurement.objects.get(pk=var_pk)
    variable = Variable.objects.get(pk=var["variable"])
    measurement.variable = variable
    measurement.value = var["value"]
    measurement.unit = var["unit"]
    measurement.place = var["place"]
    date_time = datetime.strptime(var["dateTime"], '%Y-%m-%dT%H:%M:%S.%f%z')
    measurement.dateTime = date_time
    measurement.save()
    return measurement

def create_measurement(var):
    variable = Variable.objects.get(pk=var["variable"])
    measurement = Measurement(variable=variable, value=var["value"], unit=var["unit"], place=var["place"], dateTime=var["dateTime"])
    measurement.save()
    return measurement