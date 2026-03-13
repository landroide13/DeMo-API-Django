from django.urls import path

from . import views


urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailView),

    path('Employees/', views.Employees.as_view()),
    path('Employees/<int:pk>/', views.EmployeeDetail.as_view()),
]

