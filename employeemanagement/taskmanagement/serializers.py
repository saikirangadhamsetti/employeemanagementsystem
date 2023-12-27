from .models import Task,Employee
from rest_framework import serializers

class employeeserailizer(serializers.ModelSerializer):
    assigned_tasks = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ['empid']
    def get_assigned_tasks(self,employee_instance):
        return employee_instance.task_set.filter(is_assigned=True)
        
class taskserializer(serializers.ModelSerializer):
    class Meta:
        model  = Task
        fields = "__all__"
        read_only_fields = ['taskid']

    extrakwargs={
        'employee':{"required":True},
        'title' :{'required':True}
    }
        