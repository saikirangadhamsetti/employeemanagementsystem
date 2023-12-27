from django.shortcuts import render
from .serializers import employeeserailizer,taskserializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Employee,Task
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

# Create your views here.

class CreateEmployeeView(ListCreateAPIView):
    serializer_class = employeeserailizer
    queryset = Employee.objects.all()
    
class UpdateEmployeeView(RetrieveUpdateDestroyAPIView):
    serializer_class = employeeserailizer
    queryset = Employee.objects.all()

class CreateTaskView(ListCreateAPIView):
    serializer_class = taskserializer
    queryset = Task.objects.all()
    def post(self, request, *args, **kwargs):
        if request.user.is_lead == True:
            serialize_data = taskserializer(request.data)
            if serialize_data.is_valid():
                assigned_to = serialize_data.validated_data.get("employee")
                if assigned_to.is_subordinate:
                    return super().post(request, *args, **kwargs)
                else:
                    return Response({"message":"Unable to assign tasks to leads"},status=HTTP_400_BAD_REQUEST)
            else:
                return Response({"message":"Please provide appropriate data"},status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Task cannot be created by subordinates"},status=HTTP_400_BAD_REQUEST)


class UpdateTaskView(RetrieveUpdateDestroyAPIView):
    serializer_class = taskserializer
    queryset = Task.objects.all()