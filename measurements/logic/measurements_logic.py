from ..models import Measurement

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete
    

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = new_var["variable"]
    measurement.value = new_var["value"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable=var["variable"])
    measurement = Measurement(value=var["value"])
    measurement = Measurement(unit=var["unit"])
    measurement = Measurement(place=var["place"])
    measurement = Measurement(dateTime=var["dateTime"])
    measurement.save()
    return measurement