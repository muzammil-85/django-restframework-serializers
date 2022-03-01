from api.viewsets import EmployeeViewset
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)

# url will be like this :
#   localhost:8000/api/employee/
# methods are GET , POST , PUT , DELETE