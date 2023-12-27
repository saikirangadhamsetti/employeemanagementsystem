from django.contrib import admin
from django.urls import path
from .views import CreateEmployeeView,CreateTaskView,UpdateEmployeeView,UpdateTaskView


urlpatterns = [
    path('employee/',CreateEmployeeView.as_view()),
    path('updateemployee/',UpdateEmployeeView.as_view()),
    path('tasks/',CreateTaskView.as_view()),
    path('updatetask/',UpdateTaskView.as_view())
    
]