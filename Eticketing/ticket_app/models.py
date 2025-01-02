import uuid 
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Event (models.Model):
    event_title = models.CharField(max_length= 200, unique=True)
    event_description = models.TextField('Description of event: ')
    event_date = models.DateField()
    event_time = models.TimeField ()
    event_address = models.TextField()
    event_capacity = models.IntegerField()
    event_price = models.DecimalField(max_digits=8, decimal_places=2)
    event_uuid= models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.event_title



class Ticket (models.Model):
    ticket_uuid= models.UUIDField(default=uuid.uuid4)
    event_details = models.ForeignKey(Event, on_delete= models.CASCADE)
    user_details = models.ForeignKey (User, on_delete=models.CASCADE)
    #on_delete= models.CASCADE), it delets the objects in event details, if class event is deleted
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    ticket_quantity = models.IntegerField()
    ticket_purchase_date = models.DateTimeField(default=datetime.now)
    General = 'General'
    Fanpit = 'Fanpit'
    VIP = 'VIP'
    Ticket_CHOICES = [
        (General, 'General'),
        (Fanpit, 'Fanpit'),
        (VIP, 'Vip'),
    ]
    status = models.CharField(max_length=7, choices=Ticket_CHOICES, default=General)






