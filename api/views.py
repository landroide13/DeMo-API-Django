from warnings import filters

from api.filters import EmployeeFilter
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerilizer, CommentSerilizer
from employees.models import Employee
from .serializers import StudentSerilizer, EmployeeSerilizer
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from django.shortcuts import get_object_or_404
from .pagination import CustomePagination
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter 

@api_view(['GET', 'POST'])
def studentViews(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerilizer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerilizer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerilizer(student ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class Employees(APIView):

#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerilizer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request):
#         serializer = EmployeeSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):

#     def get_object(self, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#             return employee
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerilizer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerilizer(employee ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# Mixins
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin ,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerilizer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

#Mixins
# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin ,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerilizer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)

#Generics
# class Employees(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerilizer

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerilizer
#     lookup_field = 'pk'

#ViewSet

# class EmployeesViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerilizer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = EmployeeSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerilizer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerilizer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizer
    #pagination_class = CustomePagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    #filterset_fields = ['designation']


class BlogsViews(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerilizer
    #filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title', 'blog_body']
    ordering_fields = ['blog_title']


class CommentsViews(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizer



class BlogDetailView(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerilizer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizer
    lookup_field = 'pk'