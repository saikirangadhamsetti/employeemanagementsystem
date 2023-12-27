from django.db import models

# Create your models here.
from django.db import models
import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class Employee(AbstractBaseUser):
    empid = models.CharField(max_length=10,default=None,blank=True,null=True)
    name = models.CharField(max_length=500,unique=True)
    email = models.EmailField(unique=True)
    phn = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    is_subordinate = models.BooleanField()
    is_lead = models.BooleanField()
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','is_subordinate','is_lead']

    def save(self,*args,**kwargs):
        if not self.empid:
            emp_id = 'EM'+ str(random.randint(1000, 9999))
            while Employee.objects.filter(empid=emp_id).exists():
                emp_id = 'EM'+ str(random.randint(1000, 9999))
            self.empid=emp_id
        super(Employee, self).save(*args, **kwargs)
    
class Task(models.Model):
    taskid = models.CharField(max_length=10,default=None,blank=True,null=True)
    title = models.CharField(max_length=10,default=None,blank=False,null=False)
    description = models.TextField(max_length=10,default=None,blank=True,null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    is_assigned = models.BooleanField(default=True)
    deadline = models.DateField(blank=False,null=False)
    def save(self,*args,**kwargs):
        if not self.taskid:
            task_code = 'TA'+ str(random.randint(1000, 9999))
            while Employee.objects.filter(taskid=task_code).exists():
                task_code = 'TA'+ str(random.randint(1000, 9999))
            self.taskid=task_code
        super(Task, self).save(*args, **kwargs)
    

    
    