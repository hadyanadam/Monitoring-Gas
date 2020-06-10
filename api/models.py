from django.db import models

class SensorGasModel(models.Model):
    # id = models.AutoField()
    TIANG_ID = [
        ('Tiang A',"A"),
        ('Tiang B',"B"),
        ('Tiang C',"C"),
    ]
    time_stamp = models.DateTimeField(editable =True,auto_now_add=False)
    no_tiang = models.CharField(max_length = 10,choices = TIANG_ID,default = None)
    sensor_value = models.IntegerField()
    def __str__(self):
        return f"{self.time_stamp} - {self.sensor_value}"