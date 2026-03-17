from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Employees', views.EmployeesViewSet, basename='Employees')

urlpatterns = [
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailView),

    # path('Employees/', views.Employees.as_view()),
    # path('Employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/', views.BlogsViews.as_view()),
    path('comments/', views.CommentsViews.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]

