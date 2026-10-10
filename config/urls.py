"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import Home
from web.views import PlatesRegister
from web.views import EmployeRegister
from web.views import MainView
from web.views import AdminPlates
from web.views import AdminEmpleoyee
from web.views import EditPlates
from web.views import delete_plate
from web.views import delete_employee
from web.views import admin_view
from web.views import login_view
from web.views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('admin-page/', admin_view, name='admin-page'),
    path('', Home, name='home'),
    path('plates-register/', PlatesRegister, name='plates'),
    path('employe-register/', EmployeRegister, name='employe'),
    path('main/', MainView, name='main'),
    path('admin-plates/', AdminPlates, name='admin-plates'),
    path('edit-plates/<int:id>', EditPlates, name='edit-plates'),
    path('admin-employe/', AdminEmpleoyee, name='admin-employe'),
    path('delete-plate/<int:id>/', delete_plate, name='delete-plate'),
    path('delete-employee/<int:id>/', delete_employee, name='delete-employee'),
    path('logout/', logout_view, name='logout')
]




