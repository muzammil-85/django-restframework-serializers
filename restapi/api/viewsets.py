from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset =  models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# this viewset automatically make some functions which are:
# create()
# retrieve() => only retrive one data
# list() => same as retrive but retrieve multiple data
# update()
# destroy()