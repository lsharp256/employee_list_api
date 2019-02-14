from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# API imports
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import EmployeeSerializer
from . models import Employee


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'index.html'

    def get_queryset(self):
        context = super(EmployeeListView, self).get_queryset()
        order_by = self.request.GET.get('order_by')
        if order_by:
            return context.order_by(order_by)
        return context


class CreateEmployeeView(CreateView):
    model = Employee
    template_name = 'create_employee.html'
    fields = ['first_name', 'last_name', 'job_title', 'date_started', 'description', 'photo']
    success_url = '/'


class UpdateEmployeeView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'job_title', 'description', 'photo']
    success_url = '/'
    template_name = 'update_employee.html'


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('home')
    template_name = 'confirm_delete.html'


class EmployeeList(APIView):
    """
    This class serializes all the fields from the Employee class and converts it to JSON format.
    """
    def get(self, request):
        employee_data = Employee.objects.all()
        serializer = EmployeeSerializer(employee_data, many=True)
        return Response(serializer.data)
