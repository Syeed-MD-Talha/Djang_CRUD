from django.urls import path
from .import views

urlpatterns = [
    path('',views.employee_form,name='employee_insert'), # Get and post req. for insert Operation
    path('<int:id>/',views.employee_form,name='employee_update'), # GET and POST req for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'), # GET req to redirect and display all records
]
