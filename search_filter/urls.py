
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.StudentList.as_view(), name='StudentList')
]

from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views.StudentList.as_view(), name='StudentList')
]
