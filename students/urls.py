from django.urls import include, path

from students import views

urlpatterns = [
    path('', views.students)
]

