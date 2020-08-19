from django.db import models

class Information(models.Model):
 	location = models.CharField(max_length=100)
 	incident_description = models.CharField(max_length=1000)
 	date = models.DateField()
 	time = models.TimeField()
 	incident_location = models.CharField(max_length=1000)
 	initial_severity = models.CharField(max_length=1000)
 	suspected_cause = models.CharField(max_length=1000)
 	immediate_actions_taken = models.CharField(max_length=1000)
 	sub_incident_types = models.CharField(max_length=1000)
 	reported_by = models.CharField(max_length=1000)
