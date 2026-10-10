from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from web.formularios.formPlates import FormPlates
from web.formularios.formEmployee import FormEmployee
from web.formularios.formEditPlates import FormEdit
from web.models import Platos, Empleados
from web.helpers.savePlates import savePlates
from web.helpers.saveEmployee import saveEmployee
from web.helpers.getData import getData

def Home(request):
    return render(request, 'index.html')

# Plates Register
def PlatesRegister(request):
    formulario = FormPlates()
    data = {'formulario': formulario, 'flag': False}
    savePlates(request, FormPlates, data)
    getData(data, 'platos', Platos)
    return render(request, 'registerPlates.html', data)

# Delete Plates
def delete_plate(request, id):
    plate = get_object_or_404(Platos, id=id)
    plate.delete()
    return redirect('admin-plates')

# Delete Employee
def delete_employee(request, id):
    employee = get_object_or_404(Empleados, id=id)
    employee.delete()
    return redirect('admin-employe')

# Employee Register
def EmployeRegister(request):
    formulario = FormEmployee()
    data = {'formulario': formulario, 'flag': False}
    saveEmployee(request, FormEmployee, data)
    return render(request, 'registerEmploye.html', data)

# Main View: Caffe, Drinks, Alcohol, and Food
def MainView(request):
    data = {'flag': False}

    # Fetch data for all categories
    getData(data, 'platos', Platos)
    
    # Fetch plates by category type
    caffe_items = get_deserts(Platos)      # Caffe
    drinks_items = get_deserts2(Platos)    # Drinks
    alcohol_items = get_deserts3(Platos)   # Alcohol
    food_items = get_deserts4(Platos)      # Food

    # Pass data to the context
    data["caffe"] = caffe_items
    data["drinks"] = drinks_items
    data["alcohol"] = alcohol_items
    data["food"] = food_items

    return render(request, 'getmain.html', data)

# Admin Plates
def AdminPlates(request):
    formulario = FormEdit()
    data = {'formulario': formulario, 'flag': False}
    getData(data, 'platos', Platos)
    return render(request, 'crudPlates.html', data)

# Edit Plates
def EditPlates(request, id):
    if request.method == 'POST':
        dataForm = FormEdit(request.POST)
        if dataForm.is_valid():
            dataEdit = dataForm.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(
                    nombre=dataEdit['name'],
                    descripcion=dataEdit['description'],
                    precio=dataEdit['price']
                )
            except Exception as error:
                print(error)
    return redirect('admin-plates')

# Admin Employees
def AdminEmpleoyee(request):
    data = {'flag': False}
    empleados = Empleados.objects.all()
    role_mapping = {
        1: 'Chef',
        2: 'Administrator',
        3: 'Waiter',
        4: 'Assistant',
    }
    for empleado in empleados:
        empleado.role_name = role_mapping.get(empleado.cargo, 'Unknown')
    data['empleados'] = empleados
    return render(request, 'crudEmploye.html', data)

# Authentication
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('home')

@login_required
def admin_view(request):
    return render(request, 'admin.html')

# Helper Functions
def getData(data, dataName, model):
    query = model.objects.all()
    data[dataName] = query

def get_deserts(model):
    return model.objects.filter(tipo=1)  # Caffe

def get_deserts2(model):
    return model.objects.filter(tipo=2)  # Drinks

def get_deserts3(model):
    return model.objects.filter(tipo=3)  # Alcohol

def get_deserts4(model):
    return model.objects.filter(tipo=4)  # Food
