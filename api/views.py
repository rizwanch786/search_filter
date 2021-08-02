from api.models import Student
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import StudentSerializer
from rest_framework.filters import SearchFilter
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^city']