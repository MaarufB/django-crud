from django.urls import path
from employee.views import (test)
app_name = 'employee'

urlpatterns = [
    path('test/', test, name='test')
]