from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q

def home(request):
    q = request.GET.get('q', '')
    employees = Employee.objects.filter(
        Q(name__icontains=q) | Q(email__icontains=q) |
        Q(department__icontains=q)
    )
    return render(request, "home.html", {"employees": employees})

def add_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "add.html", {"form": form})

def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    form = EmployeeForm(instance=emp)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "update.html", {"form": form})

def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect("/")
